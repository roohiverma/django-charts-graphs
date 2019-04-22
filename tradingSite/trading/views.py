from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import include, url

def index(request):
    return HttpResponse("Welcome to django charts & graphs World !!!.")