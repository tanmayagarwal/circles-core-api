from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.urls import reverse

from circlescore.models import HikayaUser

from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class HikayaUserViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            email='test@email.com',
            password='1234',
            first_name='Joe',
            last_name='Doe'
        )

    def test_hikaya_user_put(self):
        self.client.force_authenticate(self.user)

        hikaya_user = HikayaUser.objects.get(user_id=self.user.id)
        uuid = str(hikaya_user.hikaya_user_uuid)
        hikaya_user_data = model_to_dict(hikaya_user)

        hikaya_user_data['name'] = 'Joe Joe'
        hikaya_user_data['hikaya_user_uuid'] = uuid
        hikaya_user_data['user'] = reverse(
            'user-detail', kwargs={'pk': self.user.id}
        )
        response = self.client.put(
            reverse(
                'hikayauser-detail',
                kwargs={'hikaya_user_uuid': uuid}
            ),
            hikaya_user_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Joe Joe')

    def test_hikaya_user_list(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/v1/hikayauser/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)