from .models import Record
from django.contrib.auth.models import User
from rest_framework import serializers

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'user', 'discription', 'price', 'date']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =  ['url', 'username', 'email', 'groups']