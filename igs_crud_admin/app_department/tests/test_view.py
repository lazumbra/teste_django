from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TestEmployeeView(APITestCase):

    def test_add_a_departament_to_database(self):

        department_qr = {"name": "RH"}
        response = self.client.post(reverse("add_department"), department_qr)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {"name": "RH"})

    def test_add_the_same_department(self):

        department_rh = {"name": "RH"}
        self.client.post(reverse("add_department"), department_rh)
        department_rh_again = {"name": "RH"}
        response = self.client.post(
            reverse("add_department"), department_rh_again)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()["name"], [
                         "department com este name já existe."])

    def test_delete_a_department(self):

        department_rh = {"name": "RH"}
        year = "RH"
        self.client.post(
            reverse("add_department"), department_rh)

        response = self.client.delete(
            reverse("specific_department", args=["RH"]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
