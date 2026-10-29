from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.profile, name='profile'),
    path('<int:user_id>/', views.public_profile, name='public-profile'),  
]
