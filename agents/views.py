from rest_framework import viewsets
from .models import Agent, Requirement, ImplementationStrategy
from .serializers import AgentSerializer, RequirementSerializer, ImplementationStrategySerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

class ImplementationStrategyViewSet(viewsets.ModelViewSet):
    queryset = ImplementationStrategy.objects.all()
    serializer_class = ImplementationStrategySerializer