from django.shortcuts import render


def buttons(request):
    return render(request, 'buttons.html', {})


def forms(request):
    return render(request, 'forms.html', {})
