# -*- coding: utf-8 -*-

from django.test import TestCase


from rest_framework.test import APIClient

from .model_utils import agent_helper, crop_helper, market_helper, create_user


class AgentListTestCase(TestCase):
    """ Tests for the market list API. """

    def setUp(self):
        self.client = APIClient()
        self.superuser = create_user("super", superuser=True)

    def test_list_agents(self):
        """ A GET request to the agents URL should return a list of agents. """
        self.client.login(username="super", password="super_password")
        agent_helper.create()
        response = self.client.get('/v1/agents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], [{
            'person_id': u'agent-1',
            'first_name': u'Agent',
            'last_name': u'Bob',
            'address': u'10 Agent Way',
            'phone_number': 555,
            'password': u'secret-agent',
            'market': 1,
        }])

    def test_create_agent(self):
        """ A POST request to the agents URL should create an agent. """

        agent_helper.create()
        post = self.client.post('/v1/agents/', data={
            'person_id': u'agent-1',
            'first_name': u'Agent',
            'last_name': u'Bob',
            'address': u'10 Agent Way',
            'phone_number': 555,
            'password': u'secret-agent',
            'market': 1,

        })
        self.assertEqual(post.status_code, 403)


        # TODO: write the test

    def test_retrieve_an_agent(self):
        """ A GET request to an agent's URL should return the agent. """
        self.client.login(username="super", password="super_password")
        agent_helper.create()
        response = self.client.get('/v1/agents/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], [{
            'person_id': u'agent-1',
            'first_name': u'Agent',
            'last_name': u'Bob',
            'address': u'10 Agent Way',
            'phone_number': 555,
            'password': u'secret-agent',
            'market': 1,
        }])


        # TODO: write the test


class CropListTestCase(TestCase):
    """ Tests for the crop list API. """

    def setUp(self):
        self.client = APIClient()
        self.superuser = create_user("super", superuser=True)

    def test_list_crops(self):
        """ A GET request to the crops URL should return a list of crops. """
        self.client.login(username="super", password="super_password")
        crop_helper.create()
        response = self.client.get('/v1/crops/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], [{
            'id': 1,
            'crop_name': u'Crop',
            'verified': False
        }])

    # TODO: write the tests


class MarketListTestCase(TestCase):
    """ Tests for the market list API. """

    def setUp(self):
        self.client = APIClient()
        self.superuser = create_user("super", superuser=True)

    def test_list_markets(self):
        """ A GET request to the markets URL should return a list of markets. """
        self.client.login(username="super", password="super_password")
        market_helper.create()
        response = self.client.get('/v1/markets/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['results'], [{
            'market_name': u'Market',
            'id': 1,
            'town_id': 1

        }])
    # TODO: write the tests