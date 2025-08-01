from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView

from .models import Abastecimento, Tanque
from .forms import AbastecimentoForm, TanqueForm


class IndexTemplateView(TemplateView):
    template_name = 'base.html'



class ListaAbatecimentoView(ListView):
    model = Abastecimento
    queryset = Abastecimento.objects.all()
    template_name = 'listagem_abastecimentos.html'
    context_object_name = 'registros'


class AbastecimentoCreateView(CreateView):
    model = Abastecimento
    form_class = AbastecimentoForm
    template_name = 'abastecimento_form.html'
    success_url = reverse_lazy('index')


class CadastrarTanqueView(CreateView):
    model = Tanque
    form_class = TanqueForm
    template_name = 'tanque_form.html'
    success_url = reverse_lazy('index')
