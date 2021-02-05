"""UgCon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

#main urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.home, name= 'home'),
    url(r'^register/', views.register, name= 'register'),
    url(r'^flashcards/', include(('flashcards.urls','reviews'), namespace= 'flashcards')),
    url(r'^LitoAngel/', include(('LitoAngel.urls', 'reviews'), namespace= 'LitoAngel')),
    url(r'^chat/', include(('django_chatter.urls', 'reviews'), namespace ='chat')),
    url(r'^logout/', views.log_out, name = 'logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='commons/change-password.html',success_url = '/'),name='change_password'),
]
