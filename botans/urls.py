from django.urls import path
from . import rest_apis

urlpatterns = [
    path('', rest_apis.listener.as_view(), name='botcall'),
]