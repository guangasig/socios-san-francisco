from django.db import models


# Create your models here.
class Cargo(models.Model):
    cargo = models.TextField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None)
    deleted_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.cargo
