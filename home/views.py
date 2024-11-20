from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Hey, I am a Django server.</h1>
        <p>Hello this is python code</p>
        <hr>
        <h2>Not a javascript code</h2>
    """)

def sucess_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hello this is suc page</h1>")