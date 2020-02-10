from django.shortcuts import render
from django.http import HttpResponse
from .logs import logging, DEBUG

is_tracing = DEBUG

def my_test(request):
    print(is_tracing)

    if(is_tracing):
        logging("hello")

    return HttpResponse("<html>hey</html>")