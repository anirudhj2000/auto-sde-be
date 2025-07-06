from rest_framework import serializers
from .models import Agent, Requirement, ImplementationStrategy

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'

class ImplementationStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImplementationStrategy
        fields = '__all__'
