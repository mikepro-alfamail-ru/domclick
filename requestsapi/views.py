from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
import telebot

from .serializers import CustomerSerializer, StaffSerializer, RequestSerializer
from .models import Customers, Staff, Request
from .filters import RequestFilter, CustomersFilter, StaffFilter


class RequestViewSet(ModelViewSet):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RequestFilter

    def get_permissions(self):
        """Получение прав для действий."""
        permissions = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions]


class StaffViewSet(ModelViewSet):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StaffFilter

    def get_permissions(self):
        """Получение прав для действий."""
        permissions = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions]


class CustomerViewSet(ModelViewSet):

    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomersFilter

    def get_permissions(self):
        """Получение прав для действий."""
        permissions = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions]

