from django.urls import path
from django.conf.urls import url, include
from .views import (
    home, 
    # Pessoas
    lista_pessoas, 
    pessoa_novo,
    pessoa_update,

    # Veiculos
    lista_veiculos,
    veiculo_novo,
    veiculo_update,

    # Movimentos Rotativos
    lista_movrotativos,
    movrotativos_novo,
    movrotativos_update,

    # Mensalista
    lista_mensalista,
    mensalista_novo,

    # Movimentos mensalistas
    lista_movmensalista,
    movmensalista_novo
    )

urlpatterns = [
    url(r'^$', home, name='core_home'),

    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    url(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    url(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),

    url(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    url(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    url(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),

    url(r'^mov-rot/$', lista_movrotativos, name='core_lista_movrotativos'),
    url(r'^mov-rot-novo/$', movrotativos_novo, name='core_movrotativos_novo'),
    url(r'^mov-rot-update/(?P<id>\d+)/$', movrotativos_update, name='core_movrotativos_update'),

    url(r'^mensalistas/$', lista_mensalista, name='core_lista_mensalista'),
    url(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),

    url(r'^mov-mensal/$', lista_movmensalista, name='core_lista_movmensalista'),
    url(r'^mov-mensal-novo/$', movmensalista_novo, name='core_movmensalista_novo'),
]
