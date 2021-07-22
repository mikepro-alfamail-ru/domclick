import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def customers_factory():
    def factory(**kwargs):
        customer = baker.make('requestsapi.Customers', **kwargs)
        return customer
    return factory

@pytest.fixture
def staff_factory():
    def factory(**kwargs):
        staff = baker.make('requestsapi.Staff', **kwargs)
        return staff
    return factory

@pytest.fixture
def api_client():
    return APIClient()
