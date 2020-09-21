from django.conf.urls import url

from Order import views

urlpatterns=[
    url(r'^toOrder/',views.toOrder,name='toOrder'),
    url(r'^payOrder/',views.payOrder,name='payOrder'),
    url(r'^orderWeb/',views.orderWeb,name='orderWeb'),
]