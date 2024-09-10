from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    additional_info = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=20, null= True)
    
    def __str__(self):
        return self.user.first_name

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=255)
    desc = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    title = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title
    
class Link(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='links')
    telegram_username = models.CharField(max_length=255, blank=True, null=True)
    instagram_username = models.CharField(max_length=255, blank=True, null=True)
    facebook_username = models.CharField(max_length=255, blank=True, null=True)
    twitter_username = models.CharField(max_length=255, blank=True, null=True)
    linkedin_username = models.CharField(max_length=255, blank=True, null=True)
    youtube_username = models.CharField(max_length=255, blank=True, null=True)
    tiktok_username = models.CharField(max_length=255, blank=True, null=True)
    whatsapp_username = models.CharField(max_length=255, blank=True, null=True)
    github_username = models.CharField(max_length=255, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s links"

    
    def save(self, *args, **kwargs):
        print("Saving link object:", self.__dict__)
        super().save(*args, **kwargs)
    
class WebsiteStyle(models.Model):
    style_name = models.CharField(max_length=20)
