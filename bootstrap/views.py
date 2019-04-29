from django.shortcuts import render


def buttons(request):
    return render(request, 'buttons.html', {})


def forms(request):
    return render(request, 'forms.html', {})


def navbar(request):
    return render(request, 'nav_bar.html', {})


def project_copy(request):
    return render(request, 'project_main.html', {})


def project_signup(request):
    return render(request, 'project_signup.html', {})
