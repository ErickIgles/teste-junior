from django.urls import path

from .views import ListaAbatecimentoView, AbastecimentoCreateView


urlpatterns = [
    path('', ListaAbatecimentoView.as_view(), name='index'),
    path('registrar/', AbastecimentoCreateView.as_view(), name='registrar_abastecimento'),
]