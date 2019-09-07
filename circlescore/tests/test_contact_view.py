from django.urls import reverse
from django.contrib.auth import get_user_model


from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from circlescore.models import Contact


class ContactViewTest(APITestCase):
    """
    Contact View Test
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            email='test1@test.io',
            password='testpass'
        )

    def test_post_contact(self):
        self.client.force_authenticate(self.user)
        contact_data = {
            'first_name': 'Test',
            'last_name': 'Test2',
            'email': 'email@hikaya.io'
        }

        response = self.client.post(reverse('contact-list'), contact_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_contact(self):
        self.client.force_authenticate(self.user)
        contact_data = {
            'first_name': 'Contact',
            'last_name': 'Last',
            'email': 'email@hikaya.io'
        }
        Contact.objects.create(**contact_data)
        response = self.client.get(reverse('contact-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_retrieve_contact(self):
        self.client.force_authenticate(self.user)
        contact_data = {
            'first_name': 'Contact1',
            'last_name': 'Last1',
            'email': 'email@hikaya.io'
        }
        contact = Contact.objects.create(**contact_data)
        response = self.client.get(reverse(
            'contact-detail',
            kwargs={'contact_uuid': contact.contact_uuid})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], contact.first_name)

    def test_update_contact(self):
        self.client.force_authenticate(self.user)
        contact_data = {
            'first_name': 'Contact1',
            'last_name': 'Last1',
            'email': 'email@hikaya.io'
        }
        contact = Contact.objects.create(**contact_data)
        response = self.client.put(
            reverse(
                'contact-detail',
                kwargs={'contact_uuid': contact.contact_uuid}
            ),
            {'first_name': 'UpdatedName'},
            format='json'
        )

        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'UpdatedName')

    def test_delete_contact(self):
        self.client.force_authenticate(self.user)
        contact_data = {
            'first_name': 'Contact1',
            'last_name': 'Last1',
            'email': 'email@hikaya.io'
        }
        contact = Contact.objects.create(**contact_data)

        response = self.client.delete(reverse(
            'contact-detail',
            kwargs={'contact_uuid': contact.contact_uuid}
        ))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            Contact.DoesNotExist,
            Contact.objects.get,
            contact_uuid=contact.contact_uuid
        )
