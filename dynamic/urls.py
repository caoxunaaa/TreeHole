"""tree_hole URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import DynamicsList, MyDynamicsList, DynamicDelete, DynamicCreate

urlpatterns = [
    path('', DynamicsList.as_view(), name='dynamics'),
    path('my_dynamics_list', MyDynamicsList.as_view(), name='my_dynamics_list'),
    path('dynamic_delete', DynamicDelete.as_view(), name='dynamic_delete'),
    path('dynamic_create', DynamicCreate.as_view(), name='dynamic_create'),
]
