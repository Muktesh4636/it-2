"""
URL configuration for pravoo_backend project.
"""
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, "index.html")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('contact.urls')),
]

# Serve static files in development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

