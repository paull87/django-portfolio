from django.shortcuts import render


def basics(request):
    return render(request, 'css_basics.html', {})


def assessment_one(request):
    return render(request, 'assessment_one.html', {})


def fonts(request):
    return render(request, 'css_fonts.html', {})
