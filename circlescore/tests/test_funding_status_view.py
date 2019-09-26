from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model
from django.urls import reverse

from circlescore.models import FundingStatus


class FundingStatusViewSetTestCase(APITestCase):
    """
    FundingStatus View Test
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='567389'
        )

    def test_post_funding_status(self):
        """
        Test FundingStatus Post
        """
        self.client.force_authenticate(self.user)

        response = self.client.post(
            reverse('fundingstatus-list'),
            {'status': 'nop paid'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_funding_status(self):
        """
        Test FundingStatus Retrieve
        """
        self.client.force_authenticate(self.user)

        funding_status = FundingStatus.objects.create(status='rejected')

        response = self.client.get(
            reverse(
                'fundingstatus-detail',
                kwargs={'funding_status_uuid': funding_status.funding_status_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'rejected')

    def test_update_funding_status(self):
        """
        Test FundingStatus Update
        """
        self.client.force_authenticate(self.user)

        funding_status = FundingStatus.objects.create(status='rejected')

        response = self.client.put(
            reverse(
                'fundingstatus-detail',
                kwargs={'funding_status_uuid': funding_status.funding_status_uuid}
            ),
            {'status': 'denied'},
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'denied')

    def test_list_funding_status(self):
        """
        Test FundingStatus List
        """
        self.client.force_authenticate(self.user)

        FundingStatus.objects.create(status='accepted')

        response = self.client.get(reverse('fundingstatus-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_delete_funding_status(self):
        """
        Test FundingStatus Delete
        """
        self.client.force_authenticate(self.user)

        funding_status = FundingStatus.objects.create(status='test')

        response = self.client.delete(
            reverse(
                'fundingstatus-detail',
                kwargs={'funding_status_uuid': funding_status.funding_status_uuid}
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(
            FundingStatus.DoesNotExist,
            FundingStatus.objects.get,
            funding_status_uuid=funding_status.funding_status_uuid
        )
