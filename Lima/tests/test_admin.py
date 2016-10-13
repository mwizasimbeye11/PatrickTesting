# -*- coding: utf-8 -*-

from django.test import TestCase

from .model_utils import create_user


class AdminIndexTestCase(TestCase):
    def setUp(self):
        self.superuser = create_user("super", superuser=True)

    def assert_has_admin_link(self, response, model_name):
        self.assertContains(
            response,
            '<a href="/admin/Lima/%s/" class="changelink">Change</a>'
            % model_name)

    def test_admin_index(self):
        """ The admin interface should expose the correct set of models.
        """
        self.client.login(username="super", password="super_password")
        response = self.client.get('/admin/')
        self.assert_has_admin_link(response, "agent")
        self.assert_has_admin_link(response, "crop")
        self.assert_has_admin_link(response, "district")
        self.assert_has_admin_link(response, "farmer")
        self.assert_has_admin_link(response, "market")
        self.assert_has_admin_link(response, "town")
        self.assertEqual(response.status_code, 200)
