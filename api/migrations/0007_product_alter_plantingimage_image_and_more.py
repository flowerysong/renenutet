# Generated by Django 4.2.1 on 2023-06-12 06:17

import api.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_category_id_alter_cultivar_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('notes', models.TextField(blank=True)),
                ('parents', models.ManyToManyField(to='api.planting')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='plantingimage',
            name='image',
            field=models.ImageField(upload_to=api.models._image_path),
        ),
        migrations.AlterField(
            model_name='plantingimage',
            name='timestamp',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(default=datetime.date.today)),
                ('image', models.ImageField(upload_to=api.models._image_path)),
                ('description', models.TextField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
