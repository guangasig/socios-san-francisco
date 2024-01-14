from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .cargo.api.cargo_views import CargoApiViewSet
from .socio.api.socio_views import SocioViewSet

router = DefaultRouter()

# router.register(r'cargos', CargoApiViewSet, basename='cargos')
router.register(r'socios', SocioViewSet, basename='socios')

urlpatterns = [
    path('api/', include(router.urls)),
]
