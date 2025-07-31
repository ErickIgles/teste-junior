from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Abastecimento
from .forms import AbastecimentoForm

class ListaAbatecimentoView(ListView):
    model = Abastecimento
    queryset = Abastecimento.objects.all()
    template_name = 'index.html'
    context_object_name = 'registros'


class AbastecimentoCreateView(CreateView):
    model = Abastecimento
    form_class = AbastecimentoForm
    template_name = 'abastecimento_form.html'
    success_url = reverse_lazy('index')

