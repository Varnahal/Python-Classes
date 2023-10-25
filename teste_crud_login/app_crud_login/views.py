from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    return render(request,'app_crud_login/index.html')


def loginPage(request):
    return render(request,'app_crud_login/login.html')

def verificaLogin(request):
    """Verifica se o usuario esta cadastrado no sistema"""
    email = request.POST['email']
    usuario = User.objects.get(pk=1)
    return render(request,f'usuario == {usuario.name} email == {email}')


def CadastraUsuario(request):
    """Cadastra o usuario no sistema"""
    pass


def cadastro(request):
    pass