from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
import json
from django.http import JsonResponse
from utils.helpers import save_companies, save_skills, save_user_profile
def home(request):

    return render(request, 'index.html')


def mstep(request):
    
    if request.user.is_authenticated:

        if request.method == 'GET':
        
            return render(request, 'multistep.html')
        elif request.method == 'POST':
            
            print(request.POST)
            data = request.body
            data = data.decode('utf-8')
            data = json.loads(data)
            
            full_name = data['full_name']
            email = data['email']
            profession = data['profession']
            experience = data['experience']
            experiences = data['experiences']
            
            print(data)
        return JsonResponse({'message': 'Data received'},safe=False)

    else:   
        return redirect('home')

