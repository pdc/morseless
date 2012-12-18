# Create your views here.

import json
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.staticfiles.storage import staticfiles_storage

from morsecodec import morse_decode

def home(request):
    template_vars = {}

    u = staticfiles_storage.url('bookmarklet/unmorse.min.js')
    u = request.build_absolute_uri(u)
    bookmarklet_url = """
        javascript:
        void((function() {{
            var %20 d = document,
                s = d.getElementById('unmorse');
            if (s) {{
              s.parentNode.removeChild(s);
            }}
            s = d.createElement('script');
            s.setAttribute('type', 'text/javascript');
            s.setAttribute('src', '{0}');
            s.setAttribute('id', 'unmorse');
            d.body.appendChild(s);
        }})())
    """.format(u)
    bookmarklet_url = ''.join(bookmarklet_url.split())
    template_vars['bookmarklet_url'] = bookmarklet_url

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
