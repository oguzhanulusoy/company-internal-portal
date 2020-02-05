from django.shortcuts import render
from proj.app.services import person as p
# Create your views here.

def test(request):
    print(p.get_all_people())