from django.shortcuts import render

# preciso importar tanto o modelo quanto o serializer

from app_department.models import Department
from app_department.serializers import DepartmentSerializer

from rest_framework.views import APIView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def department_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def delete_department(request, pk):
    try:
        department = Department.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DepartmentSerializer(department)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
