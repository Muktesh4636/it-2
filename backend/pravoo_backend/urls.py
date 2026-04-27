"""
URL configuration for pravoo_backend project.
"""
from django.shortcuts import render, redirect
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import HttpResponse, FileResponse
import datetime
import os

admin.site.site_header = "Pravoo Admin"
admin.site.site_title = "Pravoo Admin"
admin.site.index_title = "Pravoo IT Solutions"

def home(request):
    return render(request, "index.html")

def favicon(request):
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'favicon.ico')
    return FileResponse(open(logo_path, 'rb'), content_type='image/x-icon')

def catch_all(request, path=''):
    return redirect('/', permanent=False)

def sitemap(request):
    today = datetime.date.today().isoformat()
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
  <url>
    <loc>https://pravoo.in/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://pravoo.in/#about</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pravoo.in/#services</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://pravoo.in/#portfolio</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://pravoo.in/#contact</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://pravoo.in/#faq</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://pravoo.in/#testimonials</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://the.pravoo.in/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
</urlset>"""
    return HttpResponse(xml, content_type="application/xml")

def robots(request):
    txt = """User-agent: *
Allow: /
Allow: /static/
Disallow: /admin/
Disallow: /api/
Disallow: /login/
Disallow: /accounts/
Disallow: /dashboard/
Disallow: /transaction/
Disallow: /hub/
Disallow: /panel/
Disallow: /cpanel/
Disallow: /phpmyadmin/

Sitemap: https://pravoo.in/sitemap.xml

# Pravoo IT Solutions - pravoo.in
# Web & Mobile App Development, Game Development (Unity), CRM, Custom Software
# Hyderabad, Telangana, India
"""
    return HttpResponse(txt, content_type="text/plain")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('contact.urls')),
    path('sitemap.xml', sitemap),
    path('robots.txt', robots),
    path('favicon.ico', favicon),
    re_path(r'^(?!static/)(?!admin/)(?!api/).+$', catch_all),
]

# Serve static files in development
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

