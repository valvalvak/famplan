from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('famplan.main.urls')),
    path('auth/', include('famplan.accounts.urls')),
]
