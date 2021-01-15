from django.urls import path
from django.conf.urls import url, include
from .views import home, lista_pessoas

urlpatterns = [
    url(r'^$', home, name='core_home'),
    url(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas')
]
