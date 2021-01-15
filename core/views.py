from django.shortcuts import render, redirect
from .models import (
    Pessoa, 
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)
from .forms import (
    PessoaForm, 
    VeiculoForm, 
    MovRotativoForm, 
    MensalistaForm,
    MovMensalistaForm
)


# Create your views here.
# Função para renderizar e testar
def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)


# Função que lista pessoas
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


# Função que recebe os novos dados do form
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    # Validação do formulário == obrigatório
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    # Recupera a informação do banco
    pessoa = Pessoa.objects.get(id=id)
    # Instanciar
    form = PessoaForm(request.POST or None, instance=pessoa)
    # Injetar dentro do dicionario
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


# Função que lista veiculos
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    # Validação do formulário == obrigatório
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


# Função que lista movimentos rotativos
def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'form': form, 'mov_rot': mov_rot}
    return render(request, 'core/lista_movrotativos.html', data)


def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


# Função que lista clientes mensalistas
def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalistas.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


# Função que lista movimentos dos clientes mensalistas
def lista_movmensalista(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalistas': mov_mensalistas, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalista')