from django.db import models

# Create your models here.
from django.db import models
from properties.models import Property

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.name