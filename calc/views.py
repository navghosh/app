from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'navneet'})


def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1 + val2

    return render(request, 'result.html', {'result': res})
