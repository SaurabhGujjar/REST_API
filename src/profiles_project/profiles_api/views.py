from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP method',
        'It is similar',
        'Gives you',
        'Is mapped'
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        return Response({'method':'put'})



    def patch(self, request, pk=None):
        return Response({'method':'patch'})



    def delete(self, request, pk=None):
        return Response({'method': 'delete'})



class HelloViewSet(viewsets.ViewSet):
    def list(self, request):
        a_viewset = [
        'Uses action',
        'Automatically',
        'provides'
        ]
        return Response({'a_viewset':a_viewset, 'message':'Hello!'})
