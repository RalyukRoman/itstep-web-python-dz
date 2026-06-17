from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('poems.urls')),
    path('api/', include('predictions.urls')),
    path('api/', include('randomizer.urls')),
]
