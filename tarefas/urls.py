from django.urls import path
from . import views

app_name = 'tarefas'

urlpatterns = [
path("", views.tarefas_home,),
path("adicionar/", views.adicionar_tarefas, name='adicionar')
]