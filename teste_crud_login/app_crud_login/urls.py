from django.urls import path

from . import views


app_name = "acesso"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.loginPage, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("verifica/", views.verificaLogin, name="verificaLogin"),
    path("logout/", views.logout, name="logout"),
    path("deletar/", views.deletarUser, name="deletar"),
    path("atualizar/", views.atualizarUser, name="atualizar"),
    path("atualizarDados/", views.atualizarDados, name="atualizarDados"),
    path("CadastraUsuario/", views.CadastraUsuario, name="CadastraUsuario"),
]