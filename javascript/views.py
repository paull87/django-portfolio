from django.shortcuts import render


def js_exercise3(request):
    return render(request, 'Part3_Exercise.html', {})


def runner(request):
    return render(request, 'js_runner.html', {})


def project_one(request):
    return render(request, 'Part9_JS_Project.html', {})


def arrays(request):
    return render(request, 'Part4_Array_Exercise.html', {})
