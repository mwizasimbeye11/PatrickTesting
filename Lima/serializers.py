# -*- coding: utf-8 -*-

""" Serializers for agents, crops and markets. """

from rest_framework import serializers

from .models import Agent, Crop, Market


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'
        depth = 4


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'
