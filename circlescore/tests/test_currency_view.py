from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import Currency


class CurrencyViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@user.com',
            password='21234'
        )

    def test_post_currency(self):
        """
        Test Post Currency
        """
        self.client.force_authenticate(self.user)
        currency_object = {
            'name':'US Dollar',
            'symbol': 'USD'
        }

        response = self.client.post(
            reverse('currency-list'),
            currency_object,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(response.data['name'], 'US Dollar')

    def test_retrieve_currency(self):
        """
        Test Retrieve Currency
        """
        self.client.force_authenticate(self.user)

        currency = Currency.objects.create(name='Euro', symbol='EUR')

        response = self.client.get(
            reverse('currency-detail', kwargs={'currency_uuid': currency.currency_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Euro')

    def test_list_currency(self):
        """
        Test List Currency
        """
        self.client.force_authenticate(self.user)
        Currency.objects.create(name='Rupee', symbol='RP')

        response = self.client.get(reverse('currency-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_update_currency(self):
        """
        Test Update Currency
        """
        self.client.force_authenticate(self.user)
        currency = Currency.objects.create(name='TRR', symbol='Test')

        response = self.client.put(reverse(
            'currency-detail', kwargs={'currency_uuid': currency.currency_uuid}),
            {'name': 'UGX'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'UGX')

    def test_delete_currency(self):
        """
        Test Delete Currency
        """
        self.client.force_authenticate(self.user)
        currency = Currency.objects.create(name='Test1', symbol='ADN')

        response = self.client.delete(
            reverse('currency-detail', kwargs={'currency_uuid': currency.currency_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            Currency.DoesNotExist,
            Currency.objects.get,
            currency_uuid=currency.currency_uuid
        )
