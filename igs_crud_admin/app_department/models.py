from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name
