# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from Lima.models import Agent


def create_user(username, superuser=False):
    """ Create a user. """
    if superuser:
        create = get_user_model().objects.create_superuser
    else:
        create = get_user_model().objects.create_user
    user = create(
        username, '%s@example.com' % username, '%s_password' % username)
    return user


class ModelHelper(object):
    """ Helper for building and creating instances of models. """

    # sentinel for omitting default values
    OMIT = object()

    # the model class this helper is for
    model = None

    def __init__(self, **defaults):
        self.defaults = defaults

    def _process_model_options(self, options, method):
        processed_options = {}
        for k, v in options.items():
            if isinstance(v, ModelHelper):
                v = getattr(v, method)()
            if v != self.OMIT:
                processed_options[k] = v
        return processed_options

    def build(self, **kw):
        """ Build a model instance and return it. The instance is not saved to
            the database.
        """
        build_kw = self.defaults.copy()
        build_kw.update(kw)
        build_kw = self._process_model_options(build_kw, 'build')
        return self.model(**build_kw)

    def create(self, **kw):
        """ Create a model instance and return it after saving it to the
            database.
        """
        create_kw = self.defaults.copy()
        create_kw.update(kw)
        create_kw = self._process_model_options(create_kw, 'create')
        return self.model.objects.create(**create_kw)


class AgentHelper(ModelHelper):
    model = Agent


agent_helper = AgentHelper(
    first_name="Agent",
    last_name="Bob",
    address="10 Agent Way",
    phone_number=555,
    person_id="agent-1",
    password="secret-agent",
)
