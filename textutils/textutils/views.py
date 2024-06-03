from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'index.html')

def removepunc(request):
    text = request.GET.get('text' , '')
    removepunc = request.GET.get('removepunc' , 'off')
    print(removepunc)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in text:
        if char not in punctuations:
            analyzed = analyzed + char
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitize first")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("char count")