from django.contrib import admin
from .models import Marca, Veiculo, Pessoa, Parametros

# Register your models here.

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)