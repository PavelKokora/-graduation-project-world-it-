from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Serial
from SeriesZone.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_CHAT_ID
from user_page.models import *
from django.contrib.auth.models import User
from SeriesZone.telegram import send_message_to_telegram
from SeriesZone.settings import TELEGRAM_BOT_TOKEN , TELEGRAM_BOT_CHAT_ID
# from .telegram import send_message_to_telegram

# Create your views here.

# def start(request):
    #message = f"Нове замовлення."
    #send_message_to_telegram(TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_CHAT_ID, message)




def view_search(request):
    error = False
    search_serials = request.GET.get('q', None)
    if search_serials:
        serials = Serial.objects.filter(name__iregex = search_serials )

        serials = list(serials)
        if serials == []:
            error = True

    else:
        return redirect("/catalog")

    context={
        'title':'Пошук',
        'error': error,
        'q': search_serials,
        'serials' : serials,
        'allserials' : Serial.objects.all()
            }
    
    return render(request, 'catolog/search.html', context= context)


def view_catalog(request):


    serials = Serial.objects.all()


        
    category = Category.objects.all()
    category_list = list(category)

    context={
        'title':'Головна',
        'categories': Category.objects.all(),
        'serials' : serials,
        'category_list':category_list,
        }

    return render(request, 'catolog/catalog.html', context= context)




def view_serial(request, serial_pk):

    user = request.user
    error = False
    serial = get_object_or_404(Serial, pk=serial_pk)
    season = Season.objects.filter(serial=serial)

    if 'library' in request.GET:
        if (Library.objects.filter(user=user).exists()):
            serial_list = Library.objects.get(user=user)
            serial_list.serial.add(Serial.objects.get(pk = serial_pk))
        else:
            serial_list = Library.objects.create(user=user)
            serial_list.serial.add(Serial.objects.get(pk = serial_pk))
        serial_list.save()

        return JsonResponse({"add_button":serial_pk})
    
    if 'delete_library' in request.GET:

        serial_list = Library.objects.get(user=user)
        serial_list.serial.remove(Serial.objects.get(pk = serial_pk))

        return JsonResponse({"del_button":55})
    
    

    category = Category.objects.filter(serial=serial)
    category_list = list(category)
    
    
    if not season.exists():
        error = True
        series = None
    else:
        if 'season-select' in request.GET:
            select_season = request.GET.get('season-select')
            series =  Series.objects.filter(season = season.get(number_of_season = select_season))
            series_ajax = list(series.values())
            print(series_ajax)
            return JsonResponse({"series":series_ajax})
        
        
        series =  Series.objects.filter(season = season.get(number_of_season = 1))
        first_series = series.get(number_of_series = 1)
        first_season = season.get(number_of_season = 1)
        
        # return JsonResponse({"series":series_ajax})

    if 'series_select' in request.GET:
        print(request.GET['series_select'])
        a = Series.objects.get(pk=request.GET.get('series_select'))
        # series_select_ajax = 
        # print(series_select_ajax)
        return JsonResponse({"series_data":a.video.url})
        
    # if 'serial-list' in request.GET:
    #     print(request.GET.get('serial-list'))
            


    context = {
        'first_series':first_series,
        'first_season':Series.objects.filter(season = first_season),
        'serial':serial,
        'title':serial.name,
        'season':season,
        'error':error,
        'categories':category_list,
        "in_library": Library.objects.filter(user=user,serial=serial).exists()
        
        }


    return render(request, 'catolog/view_serial.html', context)


def view_form(request, serial_pk):
    serial = get_object_or_404(Serial, pk=serial_pk)
    
    context = {
        'serial':serial
        }

    if request.method == 'POST':
        user = request.user
        card_numb = request.POST.get('cart_number')
        phone_numb = request.POST.get('phone_number')
        
        message = f'👤: {user.username},\n \n 🎬: {serial.name}, \n \n 📞: {phone_numb}, \n \n 💳: {card_numb}, \n \n ✉️:{user.email}'
        send_message_to_telegram(TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_CHAT_ID, message)

        if (Library.objects.filter(user=user).exists()):
            serial_list = Library.objects.get(user=user)
            serial_list.serial.add(serial)
        else:
            serial_list = Library.objects.create(user=user)
            serial_list.serial.add(serial)
        serial_list.save()
        
        return redirect("/user")
        




    return render(request, 'catolog/form.html', context)






        

