# Create your views here.

import json
from django.http import HttpResponse
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

def decode(request):
    results = {'success': False} # Overridden if we succeed
    morse = request.GET.get('morse')
    if morse:
        morse = morse.strip()
    if morse:
        text = morse_decode(morse)
        results['success'] = True
        results['morse'] = morse
        results['text'] = text
    return HttpResponse(json.dumps(results, indent=True), content_type='application/json')
