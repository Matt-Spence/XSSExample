"""
URL configuration for xss_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views.view import message_list, search_messages, api_messages, subtle_xss
from django.shortcuts import render

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", message_list, name="message_list"),
    path('search/', search_messages, name='search_messages'),
    path('dom-xss/', lambda request: render(request, 'dom_xss.html'), name='dom_xss'),
    path('api/messages', api_messages, name='api_messages'),
    path('subtle/', subtle_xss, name='subtle_xss'),
]
