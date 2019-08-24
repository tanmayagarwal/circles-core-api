from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from circlescore.models import AccountType


class AccountTypeTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            password='test1234',
            first_name='Joe',
            last_name='Doe'
        )

    def test_post_account_type(self):
        self.client.force_authenticate(self.user)

        type_data = {'type': 'Type 1'}
        response = self.client.post(
            reverse('accounttype-list'),
            type_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_account_type(self):
        self.client.force_authenticate(self.user)

        account_type = AccountType.objects.create(type='Type 1')
        response = self.client.put(
            reverse('accounttype-detail', kwargs={'type_uuid': account_type.type_uuid}),
            {'type': 'Type Updated'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Type Updated')

    def test_list_account_types(self):
        self.client.force_authenticate(self.user)

        AccountType.objects.create(type='Type 1')
        response = self.client.get(reverse('accounttype-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_account_type(self):
        self.client.force_authenticate(self.user)

        account_type = AccountType.objects.create(type='Type 1')
        response = self.client.delete(
            reverse('accounttype-detail', kwargs={'type_uuid': account_type.type_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            AccountType.DoesNotExist,
            AccountType.objects.get,
            type_uuid=account_type.type_uuid
        )

    def test_get_account_type_detail(self):
        self.client.force_authenticate(self.user)

        account_type = AccountType.objects.create(type='Type 1')
        response = self.client.get(
            reverse('accounttype-detail', kwargs={'type_uuid': account_type.type_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Type 1')