from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from circlescore.models import AccountSubType


class AccountTypeTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            password='test1234',
            first_name='Joe',
            last_name='Doe'
        )

    def test_post_sub_account_type(self):
        self.client.force_authenticate(self.user)

        sub_type_data = {'sub_type': 'Sub Type 1'}
        response = self.client.post(
            reverse('accountsubtype-list'),
            sub_type_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_account_sub_type(self):
        self.client.force_authenticate(self.user)

        sub_type = AccountSubType.objects.create(sub_type='Sub Type 1')
        response = self.client.put(
            reverse('accountsubtype-detail', kwargs={'sub_type_uuid': str(sub_type.sub_type_uuid)}),
            {'sub_type': 'Sub Type Updated'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sub_type'], 'Sub Type Updated')

    def test_list_account_types(self):
        self.client.force_authenticate(self.user)

        AccountSubType.objects.create(sub_type='Sub Type 1')
        response = self.client.get(reverse('accountsubtype-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_account_sub_type(self):
        self.client.force_authenticate(self.user)

        account_sub_type = AccountSubType.objects.create(sub_type='Sub Type 1')
        response = self.client.delete(
            reverse('accountsubtype-detail', kwargs={'sub_type_uuid': str(account_sub_type.sub_type_uuid)})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            AccountSubType.DoesNotExist,
            AccountSubType.objects.get,
            sub_type_uuid=account_sub_type.type_uuid
        )

    def test_get_account_sub_type_detail(self):
        self.client.force_authenticate(self.user)

        account_type = AccountSubType.objects.create(sub_type='Sub Type 1')
        response = self.client.get(
            reverse('accountsubtype-detail', kwargs={'sub_type_uuid': str(account_type.sub_type_uuid)})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sub_type'], 'Sub Type 1')