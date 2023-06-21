from django.contrib import admin

from .models import (
    Category,
    Cultivar,
    SeedSource,
    SeedPacket,
    Planting,
    PlantingImage,
    Product,
    ProductImage,
)

for mod in (
    Category,
    Cultivar,
    SeedSource,
    SeedPacket,
    Planting,
    PlantingImage,
    Product,
    ProductImage,
):
    admin.site.register(mod)
