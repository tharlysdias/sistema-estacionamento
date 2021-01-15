from django.shortcuts import render

# Create your views here.

def home(request):
    context = {'mensagem': 'Olá Mundo!'}
    return render(request, 'core/index.html', context)
