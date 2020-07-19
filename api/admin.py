from django.contrib import admin

from .models import (
    Category,
    Cultivar,
    SeedSource,
    SeedPacket,
    Planting,
    PlantingImage,
)

for mod in (
    Category,
    Cultivar,
    SeedSource,
    SeedPacket,
    Planting,
    PlantingImage,
):
    admin.site.register(mod)
