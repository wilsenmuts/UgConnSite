from django.contrib import admin
from django.conf.urls import url
from . import views
from .views import HomeView
from django.urls import path

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url('chat/?P<room_name>', views.room, name='room')
    #path('home/', HomeView.as_view(), name='blog-home')
]
