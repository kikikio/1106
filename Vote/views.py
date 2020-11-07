from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world! ")

def runoob(request):
    context= {}
    context['hello'] = 'Hello World!'
    views_name="VOTE"
    # return render(request, 'runoob.html', context)
    return render(request, 'runoob.html', {"name":views_name})