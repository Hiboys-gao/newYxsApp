from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Home.models import YxsFoodType, YxsGoods


def market(request):

    return redirect(reverse('yxshome:home'))
