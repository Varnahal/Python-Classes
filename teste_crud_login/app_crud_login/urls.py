from django.urls import path

from . import views


app_name = "acesso"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.loginPage, name="login"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("verifica/", views.verificaLogin, name="verificaLogin"),
    path("logout/", views.logout, name="logout"),
    path("CadastraUsuario/", views.CadastraUsuario, name="CadastraUsuario"),
]