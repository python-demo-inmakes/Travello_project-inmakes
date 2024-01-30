from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Victor'})


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    sumy = int(val1) + int(val2)
    return render(request, 'result.html', {
        'val1': val1,
        'val2': val2,
        'sum': sumy
    })
