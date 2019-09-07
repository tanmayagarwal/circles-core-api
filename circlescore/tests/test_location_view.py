from django.contrib.auth import get_user_model
from django.urls import  reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from circlescore.models import Location


class LocationViewTest(APITestCase):
    """
    Location View Test
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            email='test1@test.io',
            password='testpass'
        )

    def test_post_location(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            reverse('location-list'),
            {'name': 'Another Location'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_location(self):
        self.client.force_authenticate(self.user)
        Location.objects.create(name='Berlin')

        response = self.client.get(reverse('location-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_location(self):
        self.client.force_authenticate(self.user)
        location = Location.objects.create(name='London')

        response = self.client.get(reverse(
            'location-detail',
            kwargs={'location_uuid': location.location_uuid}
        ))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], location.name)

    def test_update_location(self):
        self.client.force_authenticate(self.user)
        location = Location.objects.create(name='London')
        response = self.client.put(reverse(
            'location-detail',
            kwargs={'location_uuid': location.location_uuid}),
            {'name': 'London1'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'London1')

    def test_delete_location(self):
        self.client.force_authenticate(self.user)
        location = Location.objects.create(name='London2')
        response = self.client.delete(reverse(
            'location-detail', kwargs={'location_uuid': location.location_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            Location.DoesNotExist,
            Location.objects.get,
            location_uuid=location.location_uuid
        )
