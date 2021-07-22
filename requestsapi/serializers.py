import telebot
from rest_framework import serializers

from .models import Customers, Staff, Request

from telebot_token import token

bot = telebot.TeleBot(token)


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = Customers
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'

    def update(self, instance, validated_data):
        if validated_data.get('status') is not None and instance.status != validated_data.get('status'):
            print('Haha!')
        return super(RequestSerializer, self).update(instance, validated_data)
