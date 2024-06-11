from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request , 'index.html')

def analyze(request):
    # text = request.GET.get('text' , '')
    # in GET Request we send data through our URL and our all credentials in seen the url whatever we send 
    #also GET request has a limit sending data through a url and some small server can give error
    # in Youtube when we click video tab , setting tab that is GET request and we can see in the URL Body what we sended
    # removepunc = request.GET.get('removepunc' , 'off')
    # fullcaps = request.GET.get('fullcaps' , 'off')
    # newlineremover = request.GET.get('newlineremover' , 'off')
    # extraspaceremover = request.GET.get('extraspaceremover' , 'off')
    # charcounter = request.GET.get('charcounter' , 'off')
    
    #add {% csrf_token %}  for security purpose and for post requests
    text = request.POST.get('text' , '')
    removepunc = request.POST.get('removepunc' , 'off')
    fullcaps = request.POST.get('fullcaps' , 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    extraspaceremover = request.POST.get('extraspaceremover' , 'off')
    charcounter = request.POST.get('charcounter' , 'off')
    
    
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        
        params = {"purpose" : "Removed Punctuations" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    elif(fullcaps == 'on'):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {"purpose" : "Changed to Uppercase" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    # elif(newlineremover == 'on'):
    #     analyzed = ""
    #     for char in text:
    #         if not (char == '\n'):
    #             analyzed = analyzed + char
    #     params = {"purpose" : "New Line Removed" , "analyzed_text" : analyzed}
    #     return render(request , 'analyzed.html' , params)
    elif (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        print(params)
        # Analyze the text
        return render(request, 'analyzed.html', params)
    
    elif(extraspaceremover == 'on'):
        analyzed = ""
        for index , char in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + char
        params = {"purpose" : "Extra Space Removed" , "analyzed_text" : analyzed}
        return render(request , 'analyzed.html' , params)
    
    elif(charcounter == 'on'):
        analyzed = ""
        count = 0
        for char in text:
            if not (char == " "):
                count = count + 1
        params = {"purpose" : "Number of Character" , "analyzed_text" : count}
        return render(request , 'analyzed.html' , params)
            
    else:
        return HttpResponse("Error")