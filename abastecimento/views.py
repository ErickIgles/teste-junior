from django.shortcuts import render

from django.http import HttpRequest


def index(request):
    return HttpRequest('<h1>Hello Worl!</h2>')
