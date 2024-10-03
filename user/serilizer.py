from rest_framework import serializers 
from .models import Members
 
class MembersSerialize(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = ("oname","fname","lname")