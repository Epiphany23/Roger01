from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index_view():
    return HttpResponse('这是图书管理系统')
