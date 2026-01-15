from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_submit, name='contact_submit'),
    path('newsletter/', views.newsletter_subscribe, name='newsletter_subscribe'),
]

