from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

from features.cards import views

urlpatterns = [
    re_path('cards', views.cards_view, name='cards')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
