from django.contrib import admin
from .models import Company, Profile, Skills, Link
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
@admin.register(Link)
class CustomLinkClass(ModelAdmin):
    pass
