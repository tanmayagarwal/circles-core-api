from rest_framework import status
from rest_framework.test import APIClient, APILiveServerTestCase

from django.urls import reverse
from django.contrib.auth import get_user_model

from circlescore.models import Office


class OfficeViewSetTestCase(APILiveServerTestCase):
    """
    Test office ViewSet
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            email='test@test.com'
        )

    def test_post_office(self):
        """
        Test Post Office
        """
        self.client.force_authenticate(self.user)
        office_object = {
            'name': 'Test Office 2'
        }
        response = self.client.post(
            reverse('office-list'),
            office_object,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_office(self):
        """
        Test Retrieve Office
        """
        self.client.force_authenticate(self.user)
        office = Office.objects.create(name='Test Office 3')

        response = self.client.get(
            reverse('office-detail', kwargs={'office_uuid': office.office_uuid}),
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Office 3')

    def test_list_office(self):
        """
        Test List Office
        """
        self.client.force_authenticate(self.user)
        Office.objects.create(name='Test Office 3')

        response = self.client.get(reverse('office-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_office(self):
        """
        Test Update Office
        """
        self.client.force_authenticate(self.user)
        office = Office.objects.create(name='Test Office 4')

        response = self.client.put(
            reverse('office-detail', kwargs={'office_uuid': office.office_uuid}),
            {'name': 'Test Another'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Another')

    def test_delete_office(self):
        """
        Test Delete Office
        """
        self.client.force_authenticate(self.user)
        office = Office.objects.create(name='Test Office 5')

        response = self.client.delete(
            reverse('office-detail', kwargs={'office_uuid': office.office_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            Office.DoesNotExist,
            Office.objects.get,
            office_uuid=office.office_uuid
        )
