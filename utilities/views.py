from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('We are at index function we created')
