from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('features.index.urls')),
    path('api', include('features.status.urls')),
    path('api', include('features.cards.urls'))
]
