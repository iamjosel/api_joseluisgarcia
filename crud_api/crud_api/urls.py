from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]