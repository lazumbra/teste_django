from app_department.views import (ListAllDepartament,
                                  SpecificDepartments)

from django.urls import path


urlpatterns = [
    path('', ListAllDepartament.as_view(), name="add_department"),
    path('<str:pk>/',
         SpecificDepartments.as_view(),
         name="specific_department"),
]
