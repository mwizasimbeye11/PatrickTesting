# -*- coding: utf-8 -*-

""" API for agents, crops and markets. """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.routers import DefaultRouter
from .serializers import AgentSerializer, CropSerializer, MarketSerializer
from .models import Agent, Crop, Market


class AgentViewSet(ModelViewSet):
    """ API endpoint for creating, updating and retrieving agents. """

    serializer_class = AgentSerializer
    permission_classes = (DjangoModelPermissions,)

    def get_queryset(self):
        queryset = Agent.objects.select_related()  # Needed for the REST Permissions
        agent_id = self.request.query_params.get('agent_id', None)
        password = self.request.query_params.get('password', None)
        if agent_id != None:
            if password != None:
                password = str(password)
                queryset = queryset.filter(agent_id=agent_id, password=password)
        return queryset


class CropViewSet(ModelViewSet):
    """ API endpoint for creating, updating and retrieving crops. """
    queryset = Crop.objects.all()  # Needed for the REST Permissions
    serializer_class = CropSerializer
    permission_classes = (DjangoModelPermissions,)


class MarketViewSet(ModelViewSet):
    """ API endpoint for creating, updating and retrieving crops. """
    queryset = Market.objects.all()  # Needed for the REST Permissions
    serializer_class = MarketSerializer
    permission_classes = (DjangoModelPermissions,)

api_v1 = DefaultRouter()
api_v1.register(r'agents', AgentViewSet, 'agent')
api_v1.register(r'crops', CropViewSet)
api_v1.register(r'markets', MarketViewSet)

