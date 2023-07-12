from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from user_page.models import *
from django.contrib.auth.models import User

# Create your views here.
def view_reg(request):
    
    
    context={

    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        lenght = len(password)
        regist = True
        context = {
            'password':password,
            'password_confirm':password_confirm,
            'username':username,
            'email':email,
        }
        if lenght < 8:
            context['error_text']= 'Пароль має бути більше 8!'
            regist = False
        if password != password_confirm:
            context['error_text']= 'Паролі не співпадають!'
            regist = False
        if regist:
            try:
                User.objects.create_user(username = username, password = password, email=email)
                return redirect("/auth")
            except IntegrityError:
                context['error_text']= 'Такий користувач вже існує!'
  
    return render(request,'register.html', context)
    


def view_auth(request):
    context ={
    }
    # if user.id == 0:
    #     return redirect('/catalog')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request,user)
            return redirect("/catalog")
        else:
            context['error_text'] = 'Ім`я або пароль не співпадають'
    return render(request, 'auth.html', context)


