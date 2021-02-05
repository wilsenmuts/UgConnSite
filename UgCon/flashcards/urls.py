#flashcards url
from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django .urls import path
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login, name= 'login'),
    url(r'^/view/active/', views.home, name= 'home'),
    url(r'^activity', views.activity, name ='activity' ),
    url(r'^ugbusiness', views.ugbus, name='ugbus'),
    url(r'^analysis', views.analysis, name='analysis'),
    url(r'^connect', views.connect, name='connect'),
    url(r'^apps', views.apps, name='apps'),
    url(r'^grievances', views.grievances, name='grievances'),
    url(r'^contactdev', views.contactdev, name='contactdev'),
    url(r'^contactugc', views.contactugc, name='contactugc'),
    url(r'^myactivity', views.myactivity, name='myactivity'),
    url(r'^myaccount', views.myaccount, name='myaccount'),
    url(r'decks/create/', views.createDeck, name ='createDeck'),
    url(r'^createinvestment/start', views.investmoney1, name ='investmoney'),
    url(r'^donatemoney/start', views.donatemoney1, name ='donatemoney'),
    url(r'^buyequipment/start', views.buyequipment, name ='buyequipment'),
    url(r'^buyhouse/start', views.buyhouse1, name ='buyhouse'),
    url(r'^buildhouse/start', views.buildhouse1, name ='buildhouse1'),
    url(r'^buyland/start', views.buyland1, name ='buyland'),
    url(r'^payment/start', views.payment, name ='payment'),
    url(r'^others/start', views.others1, name ='others'),
    url(r'^siteservices/start', views.siteservices, name ='siteservices'),
    url(r'downloadable/file/apk', views.apk_download, name ='apk_download'),
    #url(r'article/edit/(?P<article_id>[\d]+)', views.editdeck, name='editdeck'),
    path('search/<str:src_id>', views.sought, name='sought')
]