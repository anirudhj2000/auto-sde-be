from django.db import models
import uuid

class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Requirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.CharField(max_length=255)
    feature = models.CharField(max_length=255)
    storybook_refs = models.JSONField(default=list)
    design_tokens = models.JSONField(default=list)
    forbidden_scopes = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.page} - {self.feature}"

class ImplementationStrategy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    components_to_create_or_modify = models.JSONField(default=list)
    files_to_touch = models.JSONField(default=list)
    required_storybook_refs = models.JSONField(default=list)
    design_tokens = models.JSONField(default=list)
    estimated_steps = models.JSONField(default=list)
    success_criteria = models.TextField()
    progress_log = models.JSONField(default=list)
    clarification_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id