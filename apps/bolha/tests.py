from django.urls import reverse
from rest_framework.test import APITestCase

from apps.usuarios.tests import UsersMixin
from apps.bolha import models

"""
    Area Responsável por testar as funcionalidades da API, detectar erros e indentifica-los, de modo
    que o desenvolvimento ocorra com o minimo de erros possíveis

    Este arquivo é o responsável por testar as funcionalidades das views: "BubbleView", "CheckInView", 
    "CheckInDetailView"
"""

class BubbleTests(APITestCase, UsersMixin):
    def test_api_bubble_return_code_200(self):
        self.make_user_with_serializer('user')
        
        api_url = reverse('users:bubble:bubble', args=['user'])
        print(api_url)
        response = self.client.get(api_url)

        self.assertEqual(
            response.status_code,
            200
        )


    def test_api_bubble_return_code_404(self):
        ...