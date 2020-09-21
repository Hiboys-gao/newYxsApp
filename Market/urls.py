from django.conf.urls import url

from Market import views

urlpatterns=[
    url(r'^$',views.market),
]