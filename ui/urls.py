from django.urls import path

from . import views


urlpatterns = [
    path('', views.PlantingIndex.as_view(), name='index'),
    path('seedpackets', views.SeedPacketIndex.as_view(), name='seedpackets'),
    path('planting/<int:pk>', views.Planting.as_view(), name='planting'),
    path('product/<int:pk>', views.Product.as_view(), name='product'),
    path('seedpacket/<int:pk>', views.SeedPacket.as_view(), name='seedpacket'),
]
