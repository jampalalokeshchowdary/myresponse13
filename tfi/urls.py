from django.urls import path
from .views import *
app_name='tfi'

urlpatterns=[
    path('base/',base),
    path('home/',home),
    path('contact/',contact),
]