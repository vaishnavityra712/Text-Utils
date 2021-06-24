# I have created this file - Tyra
from django.http import HttpResponse
from django.shortcuts import render




def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcounter=request.POST.get('charcounter', 'off')
    
    
    #check which checkbox is on.

    
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    if (fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper() 
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    
    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]== " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed extraspace', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    if (charcounter=="on"):
        analyzed= ""
        analyzed = analyzed + str(len(djtext.replace(" ","")))
        params = {'purpose': 'Total Number of characters in text', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)   
        djtext=analyzed


    if(removepunc != "on" and fullcaps!="on" and extraspaceremover!="on" and charcounter=="on"):
        return HttpResponse("ERROR!!!")
    
    return render(request, 'analyze.html', params)   


    


