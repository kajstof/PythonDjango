from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'utilities/index.html')


def processed(request):
    return HttpResponse('We are at processed function we created')
