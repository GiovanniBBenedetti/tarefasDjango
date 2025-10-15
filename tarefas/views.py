from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def tarefas_home(request):
    contexto = {
        "nome":"Giovanni"
    }
    return render(request, 'tarefas/home.html', contexto)

def adicionar_tarefas(request):
    return HttpResponse("Adicionar tarefas")