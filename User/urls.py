from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^checkCode', views.checkCode, name='checkCode'),
    url(r'^checkUser', views.checkUser, name='checkUser'),
    url(r'^sende_mail', views.sende_mail),
    url(r'^logout', views.logout,name='logout'),
]
