from django.forms import ValidationError
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
import json
import time
from user.models import Company, Profile, Skills, Link
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib import messages

def about(request):
    return render(request, 'about.html')

@csrf_protect
def home(request):
    return render(request, 'index.html')

def profile(request, username):
    user = User.objects.get(username=username)
    if user is None:
        return redirect('home')
    
    profile = user.profile
    
    # Check if the logged-in user is viewing their own profile
    if request.user == user:
        return render(request, 'profile.html', {'profile': profile})
    else:
        # Render a different template for other users
        return render(request, 'public_profile.html', {'profile': profile})

@csrf_protect
@login_required
def mstep(request):
    if request.method == 'GET':
        try:
            user = request.user
            if user.profile:
                return redirect('profile', user.username)
            else:
                return render(request, 'multistep.html')
        except Exception as e:
            return render(request, 'multistep.html')

    elif request.method == 'POST':
        try:
            with transaction.atomic():
                # Update User model (for email)
                user = request.user

                # Update or create Profile
                profile, created = Profile.objects.update_or_create(
                    user=user,
                    defaults={
                        'additional_info': request.POST.get('fullname'),
                        'job': request.POST.get('profession'),
                        'location': request.POST.get('location', ''),  # Add this if you have a location field
                        'phone_number': request.POST.get('phone_number', ''),  # Add this if you have a phone number field
                    }
                )
                if request.POST.get('has_experience') == 'yes':
                    experience_count = 1
                    while True:
                        company_key = f'company_{experience_count}'
                        if company_key not in request.POST:
                            break

                        company = request.POST.get(company_key)
                        job_description = request.POST.get(f'job_description_{experience_count}')
                        start_date = request.POST.get(f'start_date_{experience_count}')
                        end_date = request.POST.get(f'end_date_{experience_count}')
                        currently_working = request.POST.get(f'currently_working_{experience_count}') == 'on'

                        if not all([company, job_description, start_date]):
                            return JsonResponse({'success': False, 'message': 'All experience fields (company, description, start date) are required.'})

                        try:
                            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
                            end_date = datetime.strptime(end_date, '%Y-%m-%d').date() if end_date and not currently_working else None
                        except ValueError:
                            return JsonResponse({'success': False, 'message': 'Invalid date format. Use YYYY-MM-DD.'})

                        Company.objects.update_or_create(
                            user=user,
                            name=company,
                            defaults={
                                'desc': job_description,
                                'start_date': start_date,
                                'end_date': end_date
                            }
                        )

                        experience_count += 1

                # Handle description (if it's part of your form)
                description = request.POST.get('description')
                if description:
                    profile.additional_info = description
                    profile.save()
                
                return redirect('profile', user.username)

        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An unexpected error occurred: {str(e)}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

@login_required
@csrf_protect
def update_profile(request):
    if request.method == 'POST':
        time.sleep(2)  # Intentional delay

        user = request.user
        profile = user.profile

        # Check if we're updating company information
        if 'company_id' in request.POST:
            company_id = request.POST.get('company_id')
            if company_id:
                try:
                    company = Company.objects.get(id=company_id, user=user)
                    company.name = request.POST.get('company_name', '').strip()
                    company.desc = request.POST.get('job_description', '').strip()
                    company.start_date = datetime.strptime(request.POST.get('start_date', ''), '%Y-%m-%d').date()
                    end_date = request.POST.get('end_date', '')
                    company.end_date = datetime.strptime(end_date, '%Y-%m-%d').date() if end_date else None
                    company.save()
                    messages.success(request, 'Company information updated successfully!')
                except Company.DoesNotExist:
                    messages.error(request, 'Company not found.')
            else:
                messages.error(request, 'No company selected for update.')
        else:
            # Update user and profile information
            user.first_name = request.POST.get('first_name', '').strip()
            user.last_name = request.POST.get('last_name', '').strip()
            user.email = request.POST.get('email', '').strip()
            profile.job = request.POST.get('job', '').strip()
            profile.location = request.POST.get('location', '').strip()
            profile.phone_number = request.POST.get('phone_number', '').strip()

            # Update or create skills
            skills = request.POST.getlist('skills')
            # Remove existing skills
            for skill in skills:
                if skill.strip():
                    Skills.objects.create(user=user, title=skill.strip())

            user.save()
            profile.save()
            messages.success(request, 'Profile updated successfully!')

        return redirect('profile', username=user.username)
    
    return redirect('profile', username=request.user.username)

@login_required
@csrf_protect
def update_user_info(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile

        user.first_name = request.POST.get('first_name', '').strip()
        user.last_name = request.POST.get('last_name', '').strip()
        user.email = request.POST.get('email', '').strip()
        profile.job = request.POST.get('job', '').strip()
        profile.location = request.POST.get('location', '').strip()
        profile.phone_number = request.POST.get('phone_number', '').strip()

        user.save()
        profile.save()
        messages.success(request, 'User information updated successfully!')

    return redirect('profile', username=request.user.username)

@login_required
@csrf_protect
def update_skills(request):
    if request.method == 'POST':
        user = request.user
        skills = request.POST.getlist('skills')
        
        # Remove existing skills
        user.skills.all().delete()
        
        # Add new skills
        for skill in skills:
            if skill.strip():
                Skills.objects.create(user=user, title=skill.strip())
        
        messages.success(request, 'Skills updated successfully!')

    return redirect('profile', username=request.user.username)

@login_required
@csrf_protect
def update_company(request):
    if request.method == 'POST':
        user = request.user
        company_id = request.POST.get('company_id')
        
        if company_id:
            company = get_object_or_404(Company, id=company_id, user=user)
            company.name = request.POST.get('company_name', '').strip()
            company.desc = request.POST.get('job_description', '').strip()
            company.start_date = datetime.strptime(request.POST.get('start_date', ''), '%Y-%m-%d').date()
            end_date = request.POST.get('end_date', '')
            company.end_date = datetime.strptime(end_date, '%Y-%m-%d').date() if end_date else None
            company.save()
            messages.success(request, 'Company information updated successfully!')
        else:
            messages.error(request, 'No company selected for update.')

    return redirect('profile', username=request.user.username)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import Link, WebsiteStyle
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def update_links(request):
    if request.method == 'POST':
        user = request.user
        link, created = Link.objects.get_or_create(user=user)
        
        platforms = request.POST.getlist('platforms[]')
        usernames = request.POST.getlist('usernames[]')
        
        for platform, username in zip(platforms, usernames):
            if platform and username:
                setattr(link, f"{platform}_username", username.strip())
            else:
                setattr(link, f"{platform}_username", None)
        
        link.save()
        
        messages.success(request, 'Social media links updated successfully!')
        
        return redirect('profile', username=user.username)
    return HttpResponseForbidden()

@login_required
def update_website_style(request):
    if request.method == 'POST':
        style_id = request.POST.get('style_name')
        try:
            style = WebsiteStyle.objects.get(id=style_id)
            request.user.profile.website_style = style
            request.user.profile.save()
        except WebsiteStyle.DoesNotExist:
            pass  # Agar tanlangan uslub topilmasa, hech narsa o'zgartirilmaydi
        
        return redirect('profile', username=request.user.username)
    return HttpResponseForbidden()

