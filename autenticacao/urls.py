from . import views
from django.urls import path

ultrapaterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
]
