from .models import Record, Tag
from django.contrib.auth.models import User
from rest_framework import serializers

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'user', 'income_or_expense', 'tag_name', 'discription', 'price', 'date']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'user', 'income_or_expense', 'tag_name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =  ['url', 'username', 'email', 'groups']