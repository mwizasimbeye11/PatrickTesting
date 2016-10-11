from rest_framework import serializers
from .models import  Agent
from .models import Crop
from .models import Market

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'
class MarketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

