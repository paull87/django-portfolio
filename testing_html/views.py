from django.shortcuts import render


def basics(request):
    return render(request, 'basics.html', {})


def lists(request):
    return render(request, 'lists.html', {})


def div_spans(request):
    return render(request, 'div_spans.html', {})
