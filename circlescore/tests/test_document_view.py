from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from circlescore.models import Document


class DocumentViewTest(APITestCase):
    """
    Document View Test
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='test',
            password='test1234',
            first_name='Joe',
            last_name='Doe'
        )

    def test_post_document(self):
        self.client.force_authenticate(self.user)
        test_document_data = {
            'name': 'test doc',
            'url': 'http://test.io'
        }
        response = self.client.post(
            reverse('document-list'),
            test_document_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_put_document(self):
        self.client.force_authenticate(self.user)

        test_document_data = {
            'name': 'test doc',
            'url': 'http://test.io'
        }
        document = Document.objects.create(**test_document_data)
        response = self.client.put(
            reverse(
                'document-detail',
                kwargs={'document_uuid': document.document_uuid}
            ),
            {'name': 'edited doc'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['document_uuid'],
                         str(document.document_uuid))

    def test_list_documents(self):
        self.client.force_authenticate(self.user)

        test_document_data = {
            'name': 'test doc',
            'url': 'http://test.io'
        }
        Document.objects.create(**test_document_data)
        response = self.client.get(reverse('document-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_document(self):
        self.client.force_authenticate(self.user)

        test_document_data = {
            'name': 'test doc',
            'url': 'http://test.io'
        }
        document = Document.objects.create(**test_document_data)
        response = self.client.delete(
            reverse(
                'document-detail',
                kwargs={'document_uuid': document.document_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            Document.DoesNotExist,
            Document.objects.get,
            document_uuid=document.document_uuid
        )

    def test_get_document_details(self):
        self.client.force_authenticate(self.user)

        test_document_data = {
            'name': 'test doc',
            'url': 'http://test.io'
        }
        document = Document.objects.create(**test_document_data)
        response = self.client.get(
            reverse(
                'document-detail',
                kwargs={'document_uuid': document.document_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], document.name)

