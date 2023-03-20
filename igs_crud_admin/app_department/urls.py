from app_department.views import (list_and_add_department,
                                  select_and_delete_department)

from django.urls import path


urlpatterns = [
    path('', list_and_add_department),
    path('<str:pk>/', select_and_delete_department),
]
