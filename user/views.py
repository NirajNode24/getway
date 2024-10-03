from django.shortcuts import render
from rest_framework import viewsets

from .serilizer import MembersSerialize
from .models import Members

class UserViewset(viewsets.ModelViewSet):
    queryset = Members.objects.all()  # Correct the spelling of "queryset"
    serializer_class = MembersSerialize
