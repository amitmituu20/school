from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from school import settings

urlpatterns = [
    
   path('',include('administrator.urls')),
   path('staff/',include('staff.urls')),
   path('staff/',include('student.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)

