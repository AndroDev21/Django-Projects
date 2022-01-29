from django.contrib.auth.models import User, Group 
from rest_framework import Serializers

class UserSerializer(Serializers.HyperlinkedModelSerializer):
     class Meta: 
         model = User 
         fields = ['url', 'username', 'email', 'groups'] 

class GroupSerializer(Serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Group
        fields = ['url', 'name'] 