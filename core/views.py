from django.shortcuts import render
from .models import (
    Pessoa, 
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

# Create your views here.

def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'core/lista_veiculos.html', {'veiculos': veiculos})


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    return render(
        request, 'core/lista_movrotativos.html', {'mov_rot': mov_rot}
    )


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    return render(
        request, 'core/lista_mensalistas.html', {'mensalistas': mensalistas}
    )


def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    return render(
        request, 'core/lista_movmensalistas.html', 
        {'mov_mensalistas': mov_mensalistas}
    )
