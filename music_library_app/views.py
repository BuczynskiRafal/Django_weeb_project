from django.shortcuts import render
from django.http import HttpResponse


def response_test(request):
    return HttpResponse("<h1>It is working</h1>")
