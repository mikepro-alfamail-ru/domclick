from django_filters import rest_framework as filters

from .models import Customers, Staff, Request


class RequestFilter(filters.FilterSet):

    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Request
        fields = ('status', 'created_at', 'updated_at', 'customer', 'staff', 'status',)


class CustomersFilter(filters.FilterSet):

    class Meta:
        model = Customers
        fields = ('name', 'email', 'id',)


class StaffFilter(filters.FilterSet):

    class Meta:
        model = Staff
        fields = ('name', 'email', 'id',)
