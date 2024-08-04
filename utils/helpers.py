from django.core.exceptions import ValidationError
from user.models import Company, Profile, Skills

def validate_data(data, field, field_name, required=True):
    value = data.get(field)
    if required and not value:
        raise ValidationError(f"{field_name} is required")
    return value

def save_user_profile(user, data):
    first_name = validate_data(data, 'first_name', 'First name')
    last_name = validate_data(data, 'last_name', 'Last name')
    job = validate_data(data, 'job', 'Job')
    email = validate_data(data, 'email', 'Email')

    profile, created = Profile.objects.create(user=user)
    profile.first_name = first_name
    profile.last_name = last_name
    profile.job = job
    profile.email = email
    profile.save()

def save_companies(user, data):
    company_names = {key: value for key, value in data.items() if key.startswith('companyname')}
    print(f"company names: {company_names}, type {type(company_names)}")
    
    for key in company_names:
        print(f"key {key}, keytype: {type(key)}")
        
        index = key.split('_')[1]
        print(f"split: {key.split('_')}")
        
        
        Company.objects.create(
            user=user,
            name=validate_data(data, key, f'Company name {index}'),
            desc=validate_data(data, f'companydesc_{index}', f'Company description {index}'),
            start_date=validate_data(data, f'companystart_{index}', f'Company start date {index}'),
            end_date=data.get(f'companyend_{index}', None)
        )

def save_skills(user, data):
    skills = [value for key, value in data.items() if key.startswith('skill')]
    for skill_name in skills:
        skill, created = Skills.objects.get_or_create(user=user)
        user.skills.add(skill)
