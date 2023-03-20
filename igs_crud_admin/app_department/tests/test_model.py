from django.test import TestCase
from app_department.models import Department


class TestEmployee(TestCase):
    def test_model_str(self):
        rh_department = Department.objects.create(name="RH")

        self.assertEqual(str(rh_department), "RH")
