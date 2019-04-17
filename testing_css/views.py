from django.shortcuts import render

def basics(request):
    return render(request, 'css_basics.html', {})
