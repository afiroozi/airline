from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.customer_list, name='index'),
]