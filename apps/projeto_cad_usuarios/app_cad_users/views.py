from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request,'users/index.html')


def listall(request):
    return render(request,'users/listall.html',{'usuarios':Usuario.objects.all()})


def usuarios(request):
    new_user = Usuario()
    new_user.nome = request.POST.get('nome')
    new_user.idade = request.POST.get('idade')
    new_user.save()
    return HttpResponseRedirect('listall')