from django.shortcuts import render


def js_exercise3(request):
    return render(request, 'Part3_Exercise.html', {})


def runner(request):
    return render(request, 'js_runner.html', {})


def project_one(request):
    return render(request, 'Part9_JS_Project.html', {})
