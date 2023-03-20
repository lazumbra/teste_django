from django.shortcuts import render

# preciso importar tanto o modelo quanto o serializer

from app_igs_employee_manager.models import Employee
from app_igs_employee_manager.serializers import EmployeeSerializer

from rest_framework.views import APIView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_all_employee(request):
    if request.method == 'GET':
        employees = {"employees": Employee.objects.all()}
        return render(request, 'employees.html', employees)


@api_view(['GET', 'DELETE'])
def delete_employee(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
