from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestEmployeeView(APITestCase):

    def setUp(self):
        department_qr = {"name": "RH"}
        self.client.post(reverse("add_department"), department_qr)

    def test_add_an_employee_to_database(self):

        employee_qr = {
            "department": "RH",
            "name": "vighhhyario",
            "email": "vigarpoiuio@calixto.com"
        }
        response = self.client.post(reverse("list_employees"), employee_qr)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_an_employee_with_incorrect_email(self):

        employee_qr = {
            "department": "RH",
            "name": "vighhhyario",
            "email": "vigarpoiuiocalixto.com"
        }
        response = self.client.post(reverse("list_employees"), employee_qr)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'], [
                         'Insira um endereço de email válido.'])

    def test_add_employee_with_no_email_to_database(self):

        employee_qr = {
            "department": "RH",
            "name": "vighhhyario"
        }
        response = self.client.post(reverse("list_employees"), employee_qr)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_adding_employee_with_no_department_added(self):

        employee_qr = {
            "department": "Armazem",
            "name": "vighhhyario",
            "email": "vigarpoiuio@calixto.com"
        }
        response = self.client.post(reverse("list_employees"), employee_qr)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
