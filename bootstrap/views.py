from django.shortcuts import render


def buttons(request):
    return render(request, 'buttons.html', {})
