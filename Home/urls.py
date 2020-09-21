from django.conf.urls import url

from Home import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^market/', views.market, name='market'),
    url(r'^mine/', views.mine, name='mine'),

]
