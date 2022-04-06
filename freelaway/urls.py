from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('auth/', include('autenticacao.urls')),
    path('jobs/', include('jobs.urls')),
    path('admin/', admin.site.urls),
]
