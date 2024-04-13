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
        'parcelas' : parcelas
    })

def add_data(request, registo_id):
    data_title = request.POST.get('data_title')
    registo = get_object_or_404(Registo, pk=registo_id, user=request.user)
    data = Registo(title=data_title, registo=registo)
    data.save()
    return HttpResponse(f'Add_data {data_title}')

def add_produto(request, registo_id):
    produto_title = request.POST.get('produto_title')
    registo = get_object_or_404(Registo, pk=registo_id, user=request.user)
    produto = Registo(title=produto_title, registo=registo)
    produto.save()
    return HttpResponse(f'Add_produto {produto_title}')

def add_dose(request, registo_id):
    dose_title = request.POST.get('dose_title')
    registo = get_object_or_404(Registo, pk=registo_id, user=request.user)
    dose = Registo(title=dose_title, registo=registo)
    dose.save()
    return HttpResponse(f'Add_produto {dose_title}')