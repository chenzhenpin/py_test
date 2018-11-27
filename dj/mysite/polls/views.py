from django.shortcuts import render,HttpResponse
from django.http import HttpResponse,request

from .models import *

# Create your views here.
def test(request):
    return HttpResponse('test')


