from django.shortcuts import render, redirect
from .forms import TarefasForm
from .models import TarefaModel
from django.http import HttpRequest
# Create your views here.


def tarefas_home(request):
    contexto = {
        "nome":"Giovanni",
        "tarefas": TarefaModel.objects.all()
    }
    return render(request, 'tarefas/home.html', contexto)


def adicionar_tarefas(request:HttpRequest):
    if request.method == "POST":
        formulario = TarefasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("tarefas:home")
    contexto = {
        "form": TarefasForm
    }
    return render(request, 'tarefas/adicionar.html', contexto)