from django.contrib import admin
from .models import Company, Profile, Skills
from unfold.admin import ModelAdmin # type: ignore


@admin.register(Profile)
class CustomProfileClass(ModelAdmin):
    pass
@admin.register(Company)
class CustomCompanyClass(ModelAdmin):
    pass
@admin.register(Skills)
class CustomSkillsClass(ModelAdmin):
    pass
