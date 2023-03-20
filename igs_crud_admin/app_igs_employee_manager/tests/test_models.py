from django.test import TestCase
from app_igs_employee_manager.models import Employee
from app_department.models import Department


class TestEmployee(TestCase):
    def test_model_str(self):
        rh_department = Department.objects.create(name="RH")
        employee = Employee.objects.create(name="Fulano",
                                           email="sicrano@fulano.com",
                                           department=rh_department)
        self.assertEqual(str(employee), "Fulano")
