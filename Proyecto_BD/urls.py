"""Proyecto_BD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mostrarIndex),
    path('form_registrar', views.mostrarFormRegistrar),
    path('listado', views.mostrarListado),
    path('form_actualizar/<int:id>', views.mostrarFormActualizar),
    path('insertar', views.insertarProducto),
    path('actualizar/<int:id>', views.actualizarProducto),
    path('eliminar/<int:id>', views.eliminarProducto)
]