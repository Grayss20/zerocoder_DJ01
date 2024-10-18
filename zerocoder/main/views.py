from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>First django app. You're at the main index.</h1>")


def data(request):
    return HttpResponse("<h1>Data text.</h1>")


def test(request):
    return HttpResponse("<h1>Test text.</h1>")
