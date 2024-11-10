from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('company.urls')),
    path('admin/', admin.site.urls),
]
