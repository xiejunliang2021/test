from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def test_css(request):
    return render(request, 'test_css.html')
