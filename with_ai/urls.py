
from django.contrib import admin
from django.urls import path, include
from ai_agent.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agent/', include('ai_agent.urls')),
    path("", home)
]
