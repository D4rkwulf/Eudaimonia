from django.urls import path

from . import views

urlpatterns = [
    path('workout-builder/', views.workout_builder, name='workout_builder'),
]
