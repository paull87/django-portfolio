from django.shortcuts import render


def basics(request):
    return render(request, 'basics.html', {})


def lists(request):
    return render(request, 'lists.html', {})


def div_spans(request):
    return render(request, 'div_spans.html', {})


def attributes(request):
    return render(request, 'attributes.html', {})


def level_one_assessment(request):
    return render(request, 'level_one_assessment.html', {})