from app_igs_employee_manager.views import (list_and_add_employee,
                                            select_and_delete_employee,
                                            list_all_employee)

from django.urls import path


urlpatterns = [
    path('', list_and_add_employee),
    path('<int:pk>/', select_and_delete_employee),
    path('list-all/', list_all_employee),
]
