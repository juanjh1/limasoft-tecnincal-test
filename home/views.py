from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index (request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "index.html")

    return render(request,"404.html")
