from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Permissão personalizada que permite leitura para qualquer usuário,
    mas permite edição e exclusão apenas para o dono do objeto.
    """

    def has_permission(self, request, view):
        # Permitir ações de leitura para todos os usuários
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Se for uma ação de escrita, o usuário deve ser o dono
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário é o dono do objeto
        return obj.owner == request.user