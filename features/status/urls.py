from django.urls import re_path

from features.status import views

urlpatterns = [
    re_path('status', views.get_status, name='status')
]
