from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_list, name='agent-list'),
    path('create/', views.agent_create, name='agent-create'),
    path('<int:pk>/', views.agent_detail, name='agent-detail'),
    path('mine/', views.my_agents_view, name='my-agents'),
    path('<int:pk>/edit/', views.agent_edit, name='agent-edit'),
    path('<int:pk>/delete/', views.agent_delete, name='agent-delete'),
]
