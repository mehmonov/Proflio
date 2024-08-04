
from django.contrib import admin
from django.urls import include, path
from home.views import home, mstep
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('mstep', mstep, name='mstep'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
