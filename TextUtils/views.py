from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check which box is on
    if (removepunc=="on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzedtext' : analyzed}
        djtext = analyzed

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
            else:
                print("no")
        params = {'purpose': 'new line remover', 'analyzedtext': analyzed}
        djtext = analyzed

    if(spaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzedtext': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Full capitalized text', 'analyzedtext': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'Full capitalized text', 'analyzedtext': analyzed}
        djtext = analyzed

    if ( removepunc!="on" and fullcaps!="on" and newlineremover !="on" and spaceremover != "on" and charcount !="on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)

