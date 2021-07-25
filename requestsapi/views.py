from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from .serializers import CustomerSerializer, StaffSerializer, RequestSerializer, RequestsTypesSerializer
from .models import Customers, Staff, Request, RequestsTypes
from .filters import RequestFilter, CustomersFilter, StaffFilter

class ModelViewSetWithPermissions(ModelViewSet):
    def get_permissions(self):
        """Получение прав для действий."""
        permissions = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions]


class RequestsTypesViewSet(ModelViewSetWithPermissions):

    queryset = RequestsTypes.objects.all()
    serializer_class = RequestsTypesSerializer


class RequestViewSet(ModelViewSetWithPermissions):

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RequestFilter


class StaffViewSet(ModelViewSetWithPermissions):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StaffFilter


class CustomerViewSet(ModelViewSetWithPermissions):

    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomersFilter
