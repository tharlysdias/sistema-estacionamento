from django.urls import path
from django.conf.urls import url, include
from .views import (
    home, 
    lista_pessoas, 
    pessoa_novo,

    lista_veiculos,
    veiculo_novo,

    lista_movrotativos,
    movrotativos_novo,

    lista_mensalista,
    mensalista_novo,

    lista_movmensalista,
    movmensalista_novo
    )

urlpatterns = [
    url(r'^$', home, name='core_home'),

    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),

    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),

    url(r'^mov-rot/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^mov-rot-novo/$', movrotativos_novo, name='core_movrotativos_novo'),

    url(r'^mensalistas/$', lista_mensalista, name='core_lista_mensalista'),
    url(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),

    url(r'^mov-mensal/$', lista_movmensalista, name='core_lista_movmensalista'),
    url(r'^mov-mensal-novo/$', movmensalista_novo, name='core_movmensalista_novo'),
]
