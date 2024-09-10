from django.contrib import admin
from django.urls import include, path
from home.views import home, mstep, profile, update_user_info, update_skills, update_company, update_links, update_website_style, about
from django.conf import settings
from django.conf.urls.static import static
def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('mstep', mstep, name='mstep'),
    path('c/<str:username>', profile, name='profile'),
    path('update-user-info/', update_user_info, name='update_user_info'),
    path('update-skills/', update_skills, name='update_skills'),
    path('update-company/', update_company, name='update_company'),
    path('update_links/', update_links, name='update_links'),
    path('update_website_style/', update_website_style, name='update_website_style'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
