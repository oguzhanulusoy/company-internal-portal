from django.shortcuts import render
from django.http import HttpResponse
from .logs import write


def my_test(request):
    write("hello")

    return HttpResponse("<html>hey</html>")