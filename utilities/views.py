from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'utilities/index.html')


def process(request):
    if request.method == 'POST':
        text = request.POST['text']
        processed = text.upper()
    return HttpResponse(processed)
