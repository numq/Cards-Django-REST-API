from django.urls import re_path

from features.index import views

urlpatterns = [
    re_path(r'^$', views.get_index, name='index')
]
