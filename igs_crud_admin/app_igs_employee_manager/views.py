from django.shortcuts import render


from app_igs_employee_manager.models import Employee
from app_igs_employee_manager.serializers import EmployeeSerializer

from rest_framework.views import APIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class EmployeeView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificEmployeeView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListAllEmployee(APIView):
    def get(self, request):
        employees = {"employees": Employee.objects.all()}
        return render(request, 'employees.html', employees)
