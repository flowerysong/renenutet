from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from api import models


class Index(generics.ListAPIView):
    queryset = models.Planting.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        data = self.queryset.filter(active=True).order_by('seed__cultivar__category__common_name', 'seed__cultivar__name')
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
        images = models.PlantingImage.objects.filter(parent=planting.id)
        return Response(
            {
                'planting': planting,
                'images': images,
            }
        )
