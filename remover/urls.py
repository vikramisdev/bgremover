from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('remove-bg/', views.remove_bg, name='remove_bg'),
]
