from django.shortcuts import render
from django.http import HttpResponse
from .logs import logging


def my_test(request):
    logging("hello")

    return HttpResponse("<html>hey</html>")