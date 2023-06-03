from django.db import models
from mdeditor.fields import MDTextField

class AppDefinition(models.Model):
    name = models.CharField(max_length=255)
    # description = models.TextField()
    description = MDTextField(null=True, blank=True)


    def __str__(self):
        return self.name


