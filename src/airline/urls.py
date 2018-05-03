from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addaircraft/', views.addAircraft, name='Add Air Craft'),
    path('report/', views.report, name='Report'),
]