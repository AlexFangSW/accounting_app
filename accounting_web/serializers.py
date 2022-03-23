from .models import Record, Tag
from django.contrib.auth.models import User
from rest_framework import serializers

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'user', 'income_or_expense', 'tag_name', 'discription', 'price', 'date']

    def update(self, instance, validated_data):

        instance.income_or_expense = validated_data['income_or_expense']
        instance.tag_name = validated_data['tag_name']
        instance.discription = validated_data['discription']
        instance.price = validated_data['price']
        instance.date = validated_data['date']

        instance.save()

        return instance


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'user', 'income_or_expense', 'tag_name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =  ['url', 'username', 'email', 'groups']