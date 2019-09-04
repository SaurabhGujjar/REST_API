# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP method',
        'It is similar',
        'Gives you',
        'Is mapped'
        ]
        return Response({'message':'Hello', 'an_apiview':an_apiview})
