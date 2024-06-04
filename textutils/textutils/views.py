from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'index.html')

def analyze(request):
    text = request.GET.get('text' , '')
    removepunc = request.GET.get('removepunc' , 'off')
    fullcaps = request.GET.get('fullcaps' , 'off')
    newlineremover = request.GET.get('newlineremover' , 'off')
    extraspaceremover = request.GET.get('extraspaceremover' , 'off')
    charcounter = request.GET.get('charcounter' , 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    if removepunc == 'on':
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {"purpose" : "Removed Punctuations" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    elif(fullcaps == 'on'):
        for char in text:
            analyzed = analyzed + char.upper()
        params = {"purpose" : "Changed to Uppercase" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    elif(newlineremover == 'on'):
        for char in text:
            if not (char == '\n'):
                analyzed = analyzed + char
        params = {"purpose" : "New Line Removed" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    elif(extraspaceremover == 'on'):
        for index , char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose" : "Extra Space Removed" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    elif(charcounter == 'on'):
        count = 0
        for char in text:
            if not (char == " "):
                count = count + 1
        params = {"purpose" : "Number of Character" , "analyzed_text" : count}
        return render(request , 'analyzed.html' , params)
            
    else:
        return HttpResponse("Error")