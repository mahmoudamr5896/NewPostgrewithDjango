"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import create_my_model, delete_my_model, edit_my_model, home, save_edit_my_model, show_my_model, update_my_model 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),  # Assign a name 'home' to the URL pattern
    path('create/', create_my_model, name='create_my_model'),
    path('show/', show_my_model, name='show_my_model'),
    path('update/<int:pk>/', update_my_model, name='update_my_model'),
    path('delete/<int:pk>/', delete_my_model, name='delete_my_model'),
    path('edit/<int:pk>/', edit_my_model, name='edit_my_model'),
    path('save_edit/<int:pk>/', save_edit_my_model, name='save_edit_my_model'),

]
