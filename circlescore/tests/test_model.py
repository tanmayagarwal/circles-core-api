from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from django.test import TestCase

from circlescore.models import *


class UserModelTest(TestCase):
    """
    Test User Model
    """
    def setUp(self):
        self.test_user_data = {
            'name': 'joedoe',
            'email': 'joedoe@circles.io',
            'password': 'joedoe1234',
            'first_name': 'Joe',
            'last_name': 'Doe'
        }

    def test_user_model_create(self):
        user = get_user_model()(
            username='test',
            email='test@test.com',
            password='test',
            first_name='Joe',
            last_name='Doe')
        user.save()
        created_user = get_user_model().objects.get(username='test')

        self.assertEqual(created_user.email, 'test@test.com')
        # Test if HikayaUser is created
        hikaya_user = HikayaUser.objects.get(user_id=created_user.id)
        self.assertEqual(hikaya_user.name, 'Joe Doe')


class GroupModelTest(TestCase):
    """
    Test Group Model
    """
    def setUp(self):
        self.test_group = {
            'name': 'Group 1'
        }

    def test_group_model_create(self):
        group = Group.objects.create(**self.test_group)
        created_group = Group.objects.get(name='Group 1')

        self.assertEqual(len(Group.objects.all()), 1)
        self.assertEqual(created_group.id, group.id)


class WorkspaceModelTest(TestCase):
    """
    Test  Workspace Model
    """
    def setUp(self):
        self.test_workspace = {'name': 'Workspace'}

    def test_workspace_model_create(self):
        workspace = Workspace.objects.create(**self.test_workspace)
        created_workspace = Workspace.objects.get(name='Workspace')

        self.assertEqual(len(Workspace.objects.all()), 1)
        self.assertEqual(created_workspace.id, workspace.id)


class DocumentModelTest(TestCase):
    def setUp(self):
        self.test_document = {'name': 'Document 1', 'url': 'http://test.com'}

    def test_document_model_create(self):
        document = Document.objects.create(**self.test_document)
        created_document = Document.objects.get(name='Document 1')

        self.assertEqual(len(Document.objects.all()), 1)
        self.assertEqual(created_document.id, document.id)