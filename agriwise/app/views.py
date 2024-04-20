from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from app.models import Parcela, Registo


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'app/app.html')
    else:
        return redirect('app_login')

def app_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app_index')
    return render(request, 'app/login.html')


def app_logout(request):
    logout(request)
    return redirect('app_login')

def parcelas_list(request, parcelas_id):
    parcelas = get_object_or_404(Parcela, pk=parcelas_id, user=request.user)
    return render(request, 'app/parcela.html', context={
        'parcelas': parcelas
    })
def add_produto_dose(request, parcelas_id):
    if request.method == 'POST':
        produto_title = request.POST.get('produto_title')
        registo = get_object_or_404(Parcela, pk=parcelas_id)
        registo.produto = produto_title
        dose_title = request.POST.get('dose_title')
        registo.dose = dose_title
        registo.save()

        return HttpResponse(f'Produto {produto_title} e dose {dose_title} adicionado à parcela {parcelas_id}')
    else:
        return HttpResponse('Acesso não permitido')

def add_parcela(request, parcelas_id):
    if request.method == 'POST':
        parcela_title = request.POST.get('parcela_title')
        registar = get_object_or_404(Parcela, pk=parcelas_id)
        registar.parcela = parcela_title
        registar.save()

        return HttpResponse(f'Parcela {parcela_title} adicionada!')
    else:
        return HttpResponse('Acesso não permitido')
