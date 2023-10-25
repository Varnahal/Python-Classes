from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app_crud_login/index.html')


def loginPage(request):
    return render(request,'app_crud_login/login.html')
