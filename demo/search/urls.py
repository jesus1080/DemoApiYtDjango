from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('list/<video_id>/',views.listV, name='tolist'),
]