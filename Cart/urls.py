from django.conf.urls import url

from Cart import views

urlpatterns=[
    url(r'^marketPlus/',views.marketPlus),
    url(r'^marketReduce/',views.marketReduce),
    url(r'^changeStatus/',views.changeStatus),
    url(r'^changeAll/',views.changeAll),
]