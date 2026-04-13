from django.urls import path

from . import views

urlpatterns = [
    path('nutrition-builder/', views.nutrition_builder, name='nutrition_builder'),
]
