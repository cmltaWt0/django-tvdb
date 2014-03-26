from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class TVDbTestCase(TestCase):
    def setUp(self):
        """
        Preconditions
        """
        self.user = User.objects.create_user('test', 'test@mail.com', 'test')
        self.client = Client()

class TVDbAuthTest(TVDbTestCase):
    """
    Testing for access to page for logged user
    and not.
    """
    def test_unauthorized_acces(self):
        """
        Should redirect to login page if not
        authentificated tvdb/.
        """
        response = self.client.get('/tvdb/', follow=True)
        self.assertEqual(response.templates[0].name, 'tvdb/login.html')

    def test_rendering_tvdb_page(self):
        """
        Should render tvdb.html template /tvdb/.
        """
        self.client.login(username='test', password='test')

        response = self.client.get('/tvdb/', follow=True)
        self.assertEqual(response.templates[0].name, 'tvdb/default_tvdb.html')

class TVDbTest(TVDbTestCase):
    """
    Common test for default behaviour,
    for selecting different column, for sorting etc.
    """
    def test_default_rendering(self):
        """
        Should render all database content by default.
        """
        self.client.login(username='test', password='test')

        response = self.client.get('/tvdb/', follow=True)
        pass
