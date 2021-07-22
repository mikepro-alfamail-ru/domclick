import pytest
import random

from .admintoken import admintoken

from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.permissions import IsAuthenticated

from requestsapi.models import Staff, Request, Customers
from requestsapi.serializers import StaffSerializer, RequestSerializer, CustomerSerializer

class DummyAuth:
    is_authenticated = True
    is_staff = True


@pytest.mark.django_db
def test_customers_retrieve(customers_factory, api_client):
    # Проверка получения пользователя
    customer = customers_factory()

    url = reverse('customers-detail', args=(customer.id,))
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert customer.name == resp_json['name']


@pytest.mark.django_db
def test_customers_list(customers_factory, api_client):
    # Проверка получения списка пользователей
    customers_factory(_quantity=4)
    url = reverse('customers-list')
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert len(resp_json) == 4


@pytest.mark.django_db
def test_customers_id_filter(customers_factory, api_client):
    '''
    проверка фильтрации списка пользователей по id и имени
    '''
    customers_factory(_quantity=5)
    names = Customers.objects.all()
    id_set = set()
    for name in names:
        id_set.add((name.id, name.name))
    id, name = random.sample(id_set, 1)[0]
    api_client.force_authenticate(user=DummyAuth, token=admintoken)

    data = {'id': id}
    url = reverse('customers-list')

    resp = api_client.get(url, data=data)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert resp_json[0]['id'] == id

    data = {'name': name}
    url = reverse('customers-list')

    resp = api_client.get(url, data=data)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert resp_json[0]['name'] == name


@pytest.mark.django_db
def test_customers_create(api_client):
    # тест успешного создания пользователя

    url = reverse('customers-list')
    name = 'Sample Customer'
    data = {'name': name}

    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.post(url, data=data)
    resp_json = resp.json()
    assert resp.status_code == HTTP_201_CREATED
    assert resp_json['name'] == name


@pytest.mark.django_db
def test_customers_update(customers_factory, api_client):
    # тест успешного обновления пользователя

    customer = customers_factory(name='Sample Customer')
    customer_id = customer.id

    new_customer_name = 'Another Customer'
    data = {'name': new_customer_name}
    url = reverse('customers-detail', args=(customer_id,))
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.put(url, data=data)
    new_customer = Customers.objects.get(id=customer_id)

    assert resp.status_code == HTTP_200_OK
    assert new_customer.name == new_customer_name


@pytest.mark.django_db
def test_customers_delete(customers_factory, api_client):
    # тест успешного удаления пользователя
    customer = customers_factory(name='Sample Customer')

    url = reverse('customers-detail', args=(customer.id,))
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.delete(url)
    assert resp.status_code == HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_staff_retrieve(staff_factory, api_client):
    # Проверка получения пользователя
    staff = staff_factory()

    url = reverse('staff-detail', args=(staff.id,))
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert staff.name == resp_json['name']


@pytest.mark.django_db
def test_staff_list(staff_factory, api_client):
    # Проверка получения списка пользователей
    staff_factory(_quantity=4)
    url = reverse('staff-list')
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert len(resp_json) == 4


@pytest.mark.django_db
def test_staff_id_filter(staff_factory, api_client):
    '''
    проверка фильтрации списка пользователей по id и имени
    '''
    staff_factory(_quantity=5)
    staff_list = Staff.objects.all()
    id_set = set()
    for name in staff_list:
        id_set.add((name.id, name.name))
    id, name = random.sample(id_set, 1)[0]
    api_client.force_authenticate(user=DummyAuth, token=admintoken)

    data = {'id': id}
    url = reverse('staff-list')

    resp = api_client.get(url, data=data)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert resp_json[0]['id'] == id

    data = {'name': name}
    url = reverse('staff-list')

    resp = api_client.get(url, data=data)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert resp_json[0]['name'] == name


@pytest.mark.django_db
def test_staff_create(api_client):
    # тест успешного создания пользователя

    url = reverse('staff-list')
    name = 'Sample Customer'
    data = {'name': name}

    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.post(url, data=data)
    resp_json = resp.json()
    assert resp.status_code == HTTP_201_CREATED
    assert resp_json['name'] == name


@pytest.mark.django_db
def test_courses_update(staff_factory, api_client):
    # тест успешного обновления пользователя

    staff = staff_factory(name='Sample Customer')
    staff_id = staff.id

    new_staff_name = 'Another Customer'
    data = {'name': new_staff_name}
    url = reverse('staff-detail', args=(staff_id,))
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.put(url, data=data)
    new_staff = Staff.objects.get(id=staff_id)

    assert resp.status_code == HTTP_200_OK
    assert new_staff.name == new_staff_name


@pytest.mark.django_db
def test_staff_delete(staff_factory, api_client):
    # тест успешного удаления пользователя
    staff = staff_factory(name='Sample Customer')

    url = reverse('staff-detail', args=(staff.id,))
    api_client.force_authenticate(user=DummyAuth, token=admintoken)
    resp = api_client.delete(url)
    assert resp.status_code == HTTP_204_NO_CONTENT
