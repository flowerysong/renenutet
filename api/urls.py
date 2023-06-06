from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description', 'friendly_name']
    friendly_name = serializers.CharField(read_only=True, source='__str__')


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class CultivarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cultivar
        fields = '__all__'


class CultivarViewSet(ReadOnlyModelViewSet):
    queryset = models.Cultivar.objects.all()
    serializer_class = CultivarSerializer


class SeedPacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SeedPacket
        fields = '__all__'


class SeedPacketViewSet(ReadOnlyModelViewSet):
    queryset = models.SeedPacket.objects.all()
    serializer_class = SeedPacketSerializer


router = DefaultRouter(trailing_slash=False)
router.register('category', CategoryViewSet)
router.register('cultivar', CultivarViewSet)
router.register('seedpacket', SeedPacketViewSet)
urlpatterns = router.urls
