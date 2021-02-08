from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('qrcode', views.qrcode)
]
