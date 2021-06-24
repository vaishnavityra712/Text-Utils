# I have created this file - Tyra
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>heya!</h1> <a href= "https://www.w3schools.com/css/css3_mediaqueries.asp" target="_blank"> Media Quaries CSS W3 schools </a>''')

# def about(request):
#     return HttpResponse("About heya!")

# pipleline for django
# def index(request):
#     return HttpResponse(''' Home  <a href="http://127.0.0.1:8000/removepunc">
#     <button>forward</button>
# </a> ''')

# def removepunc(request):
#     return HttpResponse('''remove punc <a href="http://127.0.0.1:8000/ ">
#     <button>back</button>
# </a> <a href="http://127.0.0.1:8000/capfirst">
#     <button>forward</button></a> ''')

# def capfirst(request):
#     return HttpResponse('''cap first <a href="http://127.0.0.1:8000/removepunc">
#     <button>back</button>
# </a>  ''')

# def index(request):
#     params = {'name':'avi'}
#     return render(request, 'index.html', params)

# def removepunc(request):
#     # grt the text
#     djtext = request.GET.get('text','default')
#     # print it
#     print(djtext)
#     return HttpResponse('''remove punc''')


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcounter=request.POST.get('charcounter', 'off')
    
    # return HttpResponse('''remove punc''')
    #  analyzed = djtext

    
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


    


