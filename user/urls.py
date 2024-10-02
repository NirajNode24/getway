from django.urls import path
from .views import members

urlpatterns = [
    path('member/', members,name="mem"),
]