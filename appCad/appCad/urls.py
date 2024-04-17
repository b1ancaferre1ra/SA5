from django.urls import path
from webCad.views import home, deletar, atualizar, pesquisar, cadastrar

urlpatterns = [
    path('', home, name='home'),

    path('cadastrar/', cadastrar, name='cadastrar'),

    path('atualizar/<int:id>', atualizar, name="atualizar_id"),
    path('atualizar/', atualizar, name="atualizar"),

    path('deletar/<int:id>', deletar, name="deletar_id"),
    path('deletar/', deletar, name="deletar"),

    path('pesquisar', pesquisar, name="pesquisar"),
]
