from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.bolha import models, serializers

"""
    Arquivo responsável pela lógica por trás de cada requisição HTTP, retornando a resposta adequada.

    Este arquivo contém as views da aplicação 'Bubble', que processam as requisições feitas aos endpoints
    específicos da API. As views gerenciam a interação entre a aplicação e o usuário, manipulando dados e retornando 
    as respostas no formato apropriado, como JSON, para as requisições da API.
"""

class BubbleView(APIView):
    def get(self, request, username):
        try:
            bubble = get_object_or_404(models.Bubble, user__username = username)
            serializer = serializers.BubbleSerializer(bubble)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response('A Bolha não foi encontrada', status = status.HTTP_404_NOT_FOUND)


class CheckInView(APIView):
    def get(self, request):
        ...

    def post(self, request):
        ...

class CheckInDetailView(APIView):
    def get(self,request):
        ...

    def patch(self, request):
        ...