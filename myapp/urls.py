from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AutorViewSet, LibroViewSet, home_view  # 👈 importa la nueva vista

router = DefaultRouter()
router.register(r"autores", AutorViewSet)
router.register(r"libros", LibroViewSet)

urlpatterns = [
    path("api/", include(router.urls)),  # 👈 mantiene las APIs REST
    path("", home_view, name="home"),    # 👈 nueva ruta raíz /
]
