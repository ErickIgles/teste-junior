from django.urls import path

from .views import (IndexTemplateView, 
                    ListaAbatecimentoView, 
                    AbastecimentoCreateView,
                    CadastrarTanqueView)


urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('registrar/tanque/', CadastrarTanqueView.as_view(), name='registrar_tanque'),
    path('listagem/abastecimentos/', ListaAbatecimentoView.as_view(), name='listagem_abastecimento'),
    path('registrar/', AbastecimentoCreateView.as_view(), name='registrar_abastecimento'),
]