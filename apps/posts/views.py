from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from . import models, serializers

"""
    Arquivo responsável pela lógica por trás de cada requisição HTTP, retornando a resposta adequada.

    Este arquivo contém as views de 'Posts', que processam as requisições feitas aos endpoints
    específicos da API. As views gerenciam a interação entre a aplicação e o usuário, manipulando dados e retornando 
    as respostas no formato apropriado, como JSON, para as requisições da API.
"""

class ThreadListView(APIView):
    def get(self, request):
        try:
            thread = get_list_or_404(models.Thread)
            serializer = serializers.ThreadsSerializer(thread, many = True)

            return Response(serializer.data, status= status.HTTP_200_OK)
        except NotFound:
            return Response({'detail': 'Não há Thrends cadastradas'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ThreadCreateView(APIView):
    def post(self, request):
        data = request.data

        if not data:
            return Response('Nenhum dado foi enviado!!', status = status.HTTP_400_BAD_REQUEST)
        
        try:
            serializer = serializers.ThreadsSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response("Thread criada com sucesso!!!")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': str(e) }, status=status.HTTP_400_BAD_REQUEST)
        
class ThreadDetailView(APIView):
    def get(self, request, slug):
        try:
            thread = get_object_or_404(models.Thread, slug = slug)
            serializer = serializers.ThreadsSerializer(thread)

            return Response(serializer.data, status= status.HTTP_200_OK)
        except NotFound:
            return Response({'error': 'Thrend não encontrada!!'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PostListView(APIView):
    def get(self, request):
        ...

class PostCreateView(APIView):
    def post(self, request):
        ...

class PostUpdateView(APIView):
    def patch(self, request):
        ...

class PostDeleteView(APIView):
    def delete(self, request):
        ...