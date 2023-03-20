from app_igs_employee_manager.views import (employee_list,
                                            delete_employee, list_all_employee)

from django.urls import path


urlpatterns = [
    path('', employee_list),
    path('<int:pk>/', delete_employee),
    path('list-all/', list_all_employee),
]
