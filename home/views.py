from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json

from utils.helpers import save_companies, save_skills, save_user_profile
def home(request):

    return render(request, 'index.html')


def mstep(request):
    
    if request.user.is_authenticated:

        if request.method == 'GET':
        
            return render(request, 'multistep.html')
        elif request.method == 'POST':
            
            data = request.POST # all request data
            try:
                # Foydalanuvchi profilini saqlash
                save_user_profile(request.user, data)

                # Kompaniyalarni saqlash
                save_companies(request.user, data)
    
                # Skillyarni saqlash
                save_skills(request.user, data)

                return HttpResponse("Data has been saved.")
            except Exception as e:
                return HttpResponse(f"Error: {e}")


    else:   
        return redirect('home')
