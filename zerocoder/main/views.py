from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>First django app. You're at the main index.</h1>")


def new(request):
    return HttpResponse("<h1>First django app. You're at the new index.</h1>")
