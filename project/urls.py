from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from apps.users.auth.views import LoginView,LogoutView,RefreshView

urlpatterns = [

    #URL da pagina de administrativa
    path('admin/', admin.site.urls),

    # URLs da API
    #
    # Estas são as rotas principais da API:
    # 
    # - api/posts/: Endpoints para gerenciar os posts.
    # - api/users/: Endpoints para gerenciar os usuários.
    # 
    # Cada aplicação tem suas próprias rotas, organizadas aqui.

    path('api/forum/', include("apps.forum.urls")),
    path('api/users/', include("apps.users.urls")),
    path('api/login/', LoginView.as_view(), name="login"),
    path('api/logout/', LogoutView.as_view(), name="logout"),
    path('api/refresh/', RefreshView.as_view(), name="refresh"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
