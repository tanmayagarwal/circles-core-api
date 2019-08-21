from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from django.test import TestCase


class UserModelTest(TestCase):
    def setUp(self):
        self.test_user_data = {
            'name': 'joedoe',
            'email': 'joedoe@circles.io',
            'password': 'joedoe1234'
        }

    def test_user_model_create(self):
        """
        Test User Model
        Create a user
        :return:
        """
        user = get_user_model()(username='test', email='test@test.com', password='test')
        user.save()
        created_user = get_user_model().objects.get(username='test')

        self.assertEqual(created_user.email, 'test@test.com')


class GroupModelTest(TestCase):
    def setUp(self):
        self.test_group = {
            'name': 'Group 1'
        }

    def test_group_model_create(self):
        group = Group.objects.create(**self.test_group)
        created_group = Group.objects.get(name='Group 1')

        self.assertEqual(len(Group.objects.all()), 1)
        self.assertEqual(created_group.id, group.id)