from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from api import models


class Index(generics.ListAPIView):
    queryset = models.Planting.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        data = self.get_queryset().filter(active=True).order_by('seed__cultivar__category__common_name', 'seed__cultivar__name')
        return Response(
            {
                'data': data,
            }
        )


class Planting(generics.RetrieveAPIView):
    queryset = models.Planting.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "planting.html"

    def get(self, request, *args, **kwargs):
        planting = self.get_object()
        images = models.PlantingImage.objects.filter(parent=planting.id).order_by('timestamp')
        return Response(
            {
                'planting': planting,
                'images': images,
            }
        )


class Product(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "product.html"

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        images = models.ProductImage.objects.filter(parent=product.id).order_by('timestamp')
        return Response(
            {
                'product': product,
                'images': images,
            }
        )
