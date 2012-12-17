# Create your views here.

from django.shortcuts import render

from morsecodec import morse_decode

def home(request):
    template_vars = {}
    morse = request.GET.get('morse')
    if morse:
        morse = morse.strip()
    if morse:
        text = morse_decode(morse)
        template_vars['morse'] = morse
        template_vars['text'] = text
    return render(request, 'home.html', template_vars)
