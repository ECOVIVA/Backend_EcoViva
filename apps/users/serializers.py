from rest_framework import serializers
from django.contrib.auth import password_validation
import re
from apps.bubble.models import Bubble
from . import models

"""
    Este arquivo contém os Serializers responsáveis por converter os dados dos modelos
    em JSON e vice-versa, para que possam ser usados nas APIs.

    Este arquivo é o responsavel por criar o serializer de Users, validar seus dados e fazer suas operações
    com o Banco de Dados.

"""

class UsersSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only = True)

    class Meta:
        # Classe responsavel por definir qual model o serializer vai realizar as operações, e quais campos
        # serão usados por ele.
        model = models.Users
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 'phone', 'photo']
    
    # Validação para numero de celular
    def validate_phone(self, value):
        if re.match(r'^\d{11}$', value):
            formatted_value = f"({value[:2]}) {value[2:7]}-{value[7:]}"
        elif re.match(r'^\(\d{2}\) \d{5}-\d{4}$', value):
            formatted_value = value
        else:
            raise serializers.ValidationError("Número de telefone inválido. O formato correto é (XX) XXXXX-XXXX ou 119XXXXXXXX.")
        
        return formatted_value
    
    # Validação da senha
    def validate_password(self, value):
        try:
            password_validation.validate_password(value)  # Valida conforme os validadores do Django
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"password": str(e)})
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        # Cria o usuário sem a senha
        user = super().create(validated_data)
        
        # Usa o set_password para criptografar a senha
        user.set_password(password)
        
        # Salva o usuário após definir a senha
        user.save()

        # Criação automática da bolha para o novo usuário
        bubble_data = {'user': user}
        bubble_model = Bubble.objects.create(**bubble_data)

        bubble_model.save()
            
        return user