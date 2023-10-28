from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from django.urls import reverse

# Create your views here.
def index(request):
    if request.session.has_key('logged'):
        return render(request,'app_crud_login/index.html',{'logged':True,'user_name':request.session['username']})
    else:
        return render(request,'app_crud_login/index.html')


def loginPage(request):
    return render(request,'app_crud_login/login.html')


def verificaLogin(request):
    """Verifica se o usuario esta cadastrado no sistema"""
    email = request.POST['email']
    password = request.POST['password']
    try:
        usuario = User.objects.get(email=email,password=password)
    except (User.DoesNotExist):
        return render(request,'app_crud_login/login.html',{'error_message' : 'Usuario não encontrado'})
    request.session['logged'] = True
    request.session['username'] = usuario.name
    return HttpResponseRedirect('/',{'logged':True,'user_name':usuario.name})


def logout(request):
    del request.session['logged']
    return HttpResponseRedirect('/',{'logged':False})


def CadastraUsuario(request):
    """Cadastra o usuario no sistema"""
    if request.method != 'POST':
        return HttpResponseRedirect('/acesso/cadastro')
    nome = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    if password != password2:
        return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':'as senhas não coincidem'})
    return HttpResponseRedirect('/acesso/login',{'logged':False})


def cadastro(request):
    return render(request,'app_crud_login/cadastro.html')