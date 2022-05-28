
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.front, name='front'),
    path('index',views.index, name='index'),
    path('analyze',views.analyze, name = 'analyze'),
    path('about',views.about, name = 'about'),
    path('contact',views.contact, name = 'contact'),
    path('Admin',views.Admin, name = 'Admin'),
    path('Admin_1',views.Admin_1, name = 'Admin_1'),
    path('admin_2',views.admin_2, name = 'admin_2'),
    path('invalid',views.invalid, name = 'invalid'),
   
    
    
]
