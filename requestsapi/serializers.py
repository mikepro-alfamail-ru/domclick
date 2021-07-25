from rest_framework import serializers
from django_telegrambot.apps import DjangoTelegramBot

bot = DjangoTelegramBot.get_bot()

from .models import Customers, Staff, Request, RequestsTypes


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = Customers
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = '__all__'


class RequestsTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestsTypes
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.get('customer').telegram is not None:
            chat_id = validated_data.get('customer').telegram
            bot.sendMessage(chat_id, text=f'Your request \"{validated_data.get("title")}\" was OPENED!')
        return super(RequestSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('status') is not None and instance.status != validated_data.get('status'):
            if instance.customer.telegram is not None:
                chat_id = instance.customer.telegram
                new_status = validated_data.get('status')
                bot.sendMessage(chat_id, text=f'Request \"{instance}\" status changed to {new_status}')
        return super(RequestSerializer, self).update(instance, validated_data)
