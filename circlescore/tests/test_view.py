from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status


class UserViewTest(TestCase):
    """
    Test User Endpoint
    post, list, update and delete methods
    """
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'testuser',
            'test@test.com'
        )
        self.test_user_data = {
            'username': 'joedoe',
            'first_name': 'joe',
            'last_name': 'doe',
            'email': 'joedoe@circles.io',
            'password': 'joedoe1234'
        }

    def test_post_user(self):
        response = self.client.post(
            '/api/v1/user/',
            self.test_user_data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user_authenticated(self):
        self.client.force_authenticate(self.user)
        test_user = get_user_model().objects.create_user(**self.test_user_data)
        response = self.client.patch(
            '/api/v1/user/{}/'.format(test_user.id),
            {'username': 'johndoe'}
        )
        updated_user = get_user_model().objects.get(username='johndoe')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_user.id, test_user.id)

    def test_update_user_unauthenticated(self):
        test_user = get_user_model().objects.create_user(**self.test_user_data)
        response = self.client.patch(
            '/api/v1/user/{}/'.format(test_user.id),
            {'username': 'johndoe'}
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_users_authenticated(self):
        self.client.force_authenticate(self.user)
        get_user_model().objects.create_user(**self.test_user_data)
        response = self.client.get('/api/v1/user/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_users_unauthenticated(self):
        get_user_model().objects.create_user(**self.test_user_data)
        response = self.client.get('/api/v1/user/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GroupViewTest(TestCase):
    """
    Test Group
    post, list, edit and delete,
    """
    def setUp(self):
        self.client = APIClient()
        user = self.user = get_user_model().objects.create_user(
            'testuser',
            'test@test.com'
        )

        self.client.force_authenticate(user)

        self.group_test_data = {'name': 'Test Group'}

    def test_post_group(self):
        response = self.client.post(
            '/api/v1/group/',
            self.group_test_data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_group(self):
        group = Group.objects.create(name='Test')
        response = self.client.put(
            '/api/v1/group/{}/'.format(group.id),
            {'name': 'test1'}
        )
        updated_group = Group.objects.get(name='test1')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_group.id, group.id)

    def test_list_group(self):
        Group.objects.create(name='Test')
        Group.objects.create(name='Test2')
        response = self.client.get('/api/v1/group/')

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_test_delete_group(self):
        group = Group.objects.create(name='Test2')
        response = self.client.delete('/api/v1/group/{}/'.format(group.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Group.objects.all()), 0)


class WorkspaceViewTest(TestCase):
    def setUp(self):
        pass