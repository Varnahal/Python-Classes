from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from django.contrib.auth.hashers import make_password, check_password
import re
from django.utils.translation import gettext as _


def validate_password(value):
    """Gerado pelo chat gpt para validar a senha"""
    if not re.search(r'[A-Z]', value):
        return("A senha deve conter pelo menos uma letra maiúscula.")
    elif not re.search(r'[a-z]', value):
        return("A senha deve conter pelo menos uma letra minúscula.")
    elif not re.search(r'\d', value):
        return("A senha deve conter pelo menos um número.")
    elif not re.search(r'[@#$%^&+=]', value):
        return ("A senha deve conter pelo menos um caractere especial (@, #, $, %, ^, & ou +).")
    elif len(value) < 8:
        return ("A senha deve conter pelo menos 8 caracteres.")
    else:
        return True


def index(request):
    if request.session.has_key('logged'):
        return render(request,'app_crud_login/index.html',{'logged':True,'user_name':request.session['username']})
    else:
        return render(request,'app_crud_login/index.html')


def loginPage(request):
    if request.session.has_key('logged'):
        return HttpResponseRedirect('/')
    return render(request,'app_crud_login/login.html')


def verificaLogin(request):
    """Verifica se o usuario esta cadastrado no sistema"""
    if request.method != 'POST':
        return HttpResponseRedirect('/acesso/login')
    email = request.POST['email']
    password = request.POST['password']
    try:
        usuario = User.objects.get(email=email)
    except (User.DoesNotExist):
        return render(request,'app_crud_login/login.html',{'error_message' : 'Usuario não encontrado'})
    if check_password(password, usuario.password):
        request.session['logged'] = True
        request.session['username'] = usuario.name
        return HttpResponseRedirect('/')
    else:
        return render(request,'app_crud_login/login.html',{'error_message' : 'Usuario não encontrado'})
    

def logout(request):
    if request.session.has_key('logged'):
        del request.session['logged']
    return HttpResponseRedirect('/')


def CadastraUsuario(request):
    """Cadastra o usuario no sistema"""
    try:
        #verifica se foi feita uma requisição correta
        if request.method != 'POST':
            return HttpResponseRedirect('/acesso/cadastro')
        nome = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter(email=email).count() != 0:
            return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':'Email já cadastrado, faça login'})
        if nome == '' or email == '' or password == '' or password2 == '':
            return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':'Preencha todos os campos'})
        if password != password2:
            return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':'as senhas não coincidem'})
        elif validate_password(password) != True:
            return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':validate_password(password)})
    except Exception:
        return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':'Erro interno'})
    try:
        #Criar um novo usuario no sistema
        new_user = User()
        new_user.name = nome
        new_user.email = email
        new_pass = make_password(password)
        new_user.password = new_pass
        new_user.save()
    except Exception:
        return render(request,'app_crud_login/cadastro.html',{'inpemail':email,'inpnome':nome,'error_message':'Erro ao cadastrar usuario, tente novamente'})
    return HttpResponseRedirect('/acesso/login')


def cadastro(request):
    return render(request,'app_crud_login/cadastro.html')

def perfil(request):
    if request.session.has_key('logged'):
        return render(request,'app_crud_login/perfil.html',{'logged':True,'user_name':request.session['username']})
    return HttpResponseRedirect('/')