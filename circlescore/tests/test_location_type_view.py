from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import LocationType


class LocationTypeViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@email.com',
            password='289hss'
        )

    def test_post_location_type(self):
        """
        Test LocationType Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('locationtype-list'),
            {'type': 'Type 2'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['type'], 'Type 2')

    def test_retrieve_location_type(self):
        """
        Test LocationType Retrieve
        """
        self.client.force_authenticate(self.user)
        location_type = LocationType.objects.create(type='Test')

        response = self.client.get(
            reverse(
                'locationtype-detail',
                kwargs={
                    'location_type_uuid': location_type.location_type_uuid
                }
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Test')

    def test_update_location_type(self):
        """
        Test LocationType Update
        """
        self.client.force_authenticate(self.user)
        location_type = LocationType.objects.create(type='Test1')

        response = self.client.put(
            reverse(
                'locationtype-detail',
                kwargs={'location_type_uuid': location_type.location_type_uuid}
            ),
            {'type': 'Test Edit'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['type'], 'Test Edit')

    def test_list_location_type(self):
        """
        Test LocationType List
        """
        self.client.force_authenticate(self.user)
        LocationType.objects.create(type='Test3')

        response = self.client.get(reverse('locationtype-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_location_type(self):
        """
        Test LocationType Delete
        """
        self.client.force_authenticate(self.user)
        location_type = LocationType.objects.create(type='Test')

        response = self.client.delete(
            reverse(
                'locationtype-detail',
                kwargs={'location_type_uuid': location_type.location_type_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            LocationType.DoesNotExist,
            LocationType.objects.get,
            location_type_uuid=location_type.location_type_uuid
        )
