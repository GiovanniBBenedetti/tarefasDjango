from django.http import HttpResponse


def teste_view(request):
    return HttpResponse("Essa é a porta de teste")


def index_view(request):
    return HttpResponse("<h1>Bem-vindo</h1>")
