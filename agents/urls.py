from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, RequirementViewSet, ImplementationStrategyViewSet

router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'requirements', RequirementViewSet)
router.register(r'strategies', ImplementationStrategyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
