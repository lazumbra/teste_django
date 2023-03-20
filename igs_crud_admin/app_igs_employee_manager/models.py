from django.db import models


from app_department.models import Department


class Employee(models.Model):
    department = models.ForeignKey(
        Department,  on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
