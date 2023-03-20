from app_igs_employee_manager.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["department", "name", "email"]
