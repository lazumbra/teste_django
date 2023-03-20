from app_department.views import department_list, delete_department

from django.urls import path


urlpatterns = [
    path('', department_list),
    path('<str:pk>/', delete_department),
]
