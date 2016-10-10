from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response  import Response
from serializers import AgentSerializer
from models import Agent

class AgentList(APIView):

    def get(self,request):
        agent = Agent.objects.all()
        serializer = AgentSerializer(agent,many=True)
        return Response(serializer.data)
    def post(self,request):
        pass


# Create your views here.
