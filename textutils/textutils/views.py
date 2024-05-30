from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print(request.GET.get('text' , 'default'))
    return render(request , 'index.html')

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitize first")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("char count")