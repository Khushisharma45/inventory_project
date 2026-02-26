from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),  # Web UI
    path('api/', include('inventory.api_urls')),  # REST API
]
