from django.shortcuts import render


def capstone_welcome(request):
    return render(request, 'capstone_welcome.html', {})

def capstone_thankyou(request):
    return render(request, 'capstone_thankyou.html', {})
