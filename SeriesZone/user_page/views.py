from django.shortcuts import render, redirect
from catalog.models import *
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def view_user(request):
    user = request.user



    if user.id == None or user.id == 1:
        return redirect('login')
    else:
        # my_user = My_User.objects.get(user=user)
        if (Library.objects.filter(user=user).exists()):
            user_library = Library.objects.get(user=user)
            user_serials = user_library.serial.all()
        else:
            user_serials = None
        
        
        context = {
            'title':'Профіль',
            'name': user.username,
            "user_serials":user_serials,  
        }

    return render(request, 'profile/profile.html' , context)

