from django.urls import path
from ai_agent.views import chat_page, chat_api

urlpatterns = [
    path('', chat_page, name='agent-page'),
    path('chat/', chat_api, name='agent-chat'),
]