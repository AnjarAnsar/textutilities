from django.http import HttpResponse
from django.shortcuts import render

def getstarted(request):
    return render(request, 'index.html')

def analyse(request):
    djtext = request.GET.get('name', 'anzar')  # Retrieves the 'name' parameter from the request
    removepunc = request.GET.get('removepunc', 'off')  # Retrieves the 'removepunc' parameter from the request
    capitalise = request.GET.get('uppercase', 'off')
    newline = request.GET.get('newlineremov', 'off')
    count = 0
    print(djtext)
    for i in range(0, len(djtext)):
        count = count + 1

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed_text = ""
        for char in djtext:
            if char not in punctuations:
                analysed_text += char

        params = {'purpose': 'Remove punctuation', 'analysed_text': analysed_text, 'number': count}
        djtext=analysed_text
        # return render(request, 'analyse.html', params)

    if capitalise == 'on':
        analysed_text = ""
        for char in djtext:
            analysed_text += char.upper()

        params = {'purpose': 'capitalise', 'analysed_text': analysed_text, 'number': count}
        djtext=analysed_text

        # return render(request, 'analyse.html', params)

    if newline == 'on':
        analysed_text = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analysed_text += char

        params = {'purpose': 'newline', 'analysed_text': analysed_text, 'number': count}




    if(removepunc != 'on' and capitalise != 'on' and newline != 'on'  ):
        return HttpResponse(f"You did not select anything. Analysed text = input text that is {djtext}")

    return render(request, 'analyse.html', params)


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

