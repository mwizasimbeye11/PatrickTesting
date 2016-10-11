from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response  import Response
from serializers import AgentSerializer
from serializers import CropSerializer
from serializers import MarketsSerializer
from models import Agent
from models import Market
from models import Crop

class AgentList(APIView):

    def get(self,request):
        agent = Agent.objects.all()
        serializer = AgentSerializer(agent,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass

class CropList(APIView):
    def get(self, request):
        crop = Crop.objects.all()
        serializer = CropSerializer(crop, many=True)
        return Response(serializer.data)

    def post(self, request , format = None):
        serializer = AgentSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarketList(APIView):
    def get(self, request):
        market = Market.objects.all()
        serializer = MarketsSerializer(market , many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

# Create your views here.
