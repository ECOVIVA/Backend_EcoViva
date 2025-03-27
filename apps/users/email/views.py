from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Users
from .tokens import email_confirmation_token

class EmailConfirmAPIView(APIView):
    def get(self, request, uidb64, token):
        try:
            # Decodifica o ID do usuário
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_object_or_404(Users, pk=uid)

            # Verifica se o token é válido
            if email_confirmation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"message": "E-mail confirmado com sucesso!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Token inválido ou expirado."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
