from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('planting/<int:pk>', views.Planting.as_view(), name='planting'),
]
