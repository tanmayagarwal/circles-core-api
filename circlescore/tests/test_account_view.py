from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import Account


class AccountViewSetTestCase(APITestCase):
    """
    Test Account ViewSet
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='gcdhsjwo'
        )

    def test_post_account(self):
        """
        Test Account Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('account-list'),
            {'full_name': 'Account 1'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], 'Account 1')

    def test_retrieve_account(self):
        """
        Test Account Retrieve
        """
        self.client.force_authenticate(self.user)
        account = Account.objects.create(full_name='Account 2')

        response = self.client.get(
            reverse(
                'account-detail',
                kwargs={'account_uuid': account.account_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'Account 2')

    def test_update_account(self):
        """
        Test Account Update
        """
        self.client.force_authenticate(self.user)

        account = Account.objects.create(full_name='Account 3')

        response = self.client.put(
            reverse(
                'account-detail',
                kwargs={'account_uuid': account.account_uuid}
            ),
            {'full_name': 'Account Update'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], 'Account Update')

    def test_list_account(self):
        """
        Test Account List
        """
        self.client.force_authenticate(self.user)
        Account.objects.create(full_name='Account 5')

        response = self.client.get(reverse('account-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_account(self):
        """
        Test Account Delete
        """
        self.client.force_authenticate(self.user)

        self.client.force_authenticate(self.user)

        account = Account.objects.create(full_name='Account 6')

        response = self.client.delete(
            reverse(
                'account-detail',
                kwargs={'account_uuid': account.account_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            Account.DoesNotExist,
            Account.objects.get,
            account_uuid=account.account_uuid
        )
