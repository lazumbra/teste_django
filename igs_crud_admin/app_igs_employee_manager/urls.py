from app_igs_employee_manager.views import (EmployeeView,
                                            SpecificEmployeeView,
                                            ListAllEmployee)

from django.urls import path


urlpatterns = [
    path('', EmployeeView.as_view(), name="list_employees"),
    path('<int:pk>/', SpecificEmployeeView.as_view(), name="specif_employees"),
    path('list-all/', ListAllEmployee.as_view(), name="list_all_employees"),
]
