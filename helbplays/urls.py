from django.urls import path
from . import views

urlpatterns = [
    path('', views.helbplays_home, name='helbplays-home'),
]
