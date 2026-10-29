from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.chat_view, name='chat-view'),
    path("api/<int:pk>/", views.chat_messages_api, name="chat-messages-api"),
]
