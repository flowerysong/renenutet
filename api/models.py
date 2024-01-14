import subprocess
import uuid

from datetime import date

from django.db import models
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


def _image_path(instance, filename):
    ext = filename.split('.')[-1]
    if len(ext) > 4:
        ext = 'jpg'
    return f'images/{uuid.uuid4()}.{ext}'


class Base(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.name


class BaseImage(models.Model):
    class Meta:
        abstract = True

    timestamp = models.DateField(default=date.today)
    image = models.ImageField(upload_to=_image_path)
    description = models.TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # save the filename so that we know whether it's new later on
        self._original_image_file = self.image.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image and self.image.name != self._original_image_file:
            # save the new name
            self._original_image_file = self.image.name
            # strip the metadata
            subprocess.run(['exiftool', '-gps*=', '-overwrite_original', self.image.path])


class Category(MPTTModel):
    class Meta:
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=512, unique=True)
    common_name = models.CharField(max_length=512, blank=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        nodes = []
        for x in self.get_ancestors(include_self=True):
            if x.common_name:
                nodes.append('{} ({})'.format(x.common_name, x.name))
            else:
                nodes.append(x.name)
        return ' / '.join(nodes)

    def cn(self):
        for x in reversed(self.get_ancestors(include_self=True)):
            if x.common_name:
                return x.common_name
        return None


class Cultivar(Base):
    class Meta:
        ordering = ['category__common_name', 'name']

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField()
    aliases = models.JSONField(default=list, blank=True, null=False)

    def __str__(self):
        cat = self.category.cn()
        if cat and cat != self.name:
            return '{}, {}'.format(cat, self.name)
        return self.name


class SeedSource(Base):
    class Meta:
        verbose_name_plural = 'Seed sources'

    url = models.URLField(max_length=256, blank=True)
    description = models.TextField()


class SeedPacket(models.Model):
    class Meta:
        ordering = ['-active', '-date', 'cultivar']
        verbose_name_plural = 'Seed packets'

    date = models.DateField(default=date.today)
    cultivar = models.ForeignKey(Cultivar, on_delete=models.PROTECT)
    source = models.ForeignKey(SeedSource, on_delete=models.PROTECT)
    source_planting = models.ForeignKey('Planting', on_delete=models.PROTECT, null=True, blank=True)
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} ({self.cultivar.category.common_name}, {self.cultivar.name}) ({self.source.name})'


class Planting(models.Model):
    class Meta:
        ordering = ['-active', '-date', 'seed']

    date = models.DateField(default=date.today)
    seed = models.ForeignKey(SeedPacket, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return '{} ({})'.format(self.seed, self.date)


class PlantingImage(BaseImage):
    parent = models.ForeignKey(Planting, on_delete=models.CASCADE)


class Product(Base):
    parents = models.ManyToManyField(Planting)
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True)


class ProductImage(BaseImage):
    parent = models.ForeignKey(Product, on_delete=models.CASCADE)
