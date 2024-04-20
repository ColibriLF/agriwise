from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, html_content=None):
    return render(request, 'website/inicio.html')