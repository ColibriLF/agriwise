from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request, html_content=None):
    if html_content is None:
        html_content = (
            '<h1>Agriwise Website</h1>'
            '<a href="/app/login/"><button>Faça Login</button></a>'
        )
    return HttpResponse(html_content)