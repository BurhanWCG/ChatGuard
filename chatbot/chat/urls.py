
from django.urls import path
from chat import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot_view'),
]
