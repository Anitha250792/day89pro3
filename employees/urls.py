from django.urls import path
from .views import (
    EmployeeListView, EmployeeCreateView, EmployeeUpdateView,
    employee_detail, employee_delete,
    EmployeeListCreateAPI, employee_retrieve_delete_api
)

urlpatterns = [
    # HTML pages
    path('', EmployeeListView.as_view(), name='employee_list'),
    path('employee/add/', EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employee/<int:pk>/', employee_detail, name='employee_detail'),
    path('employee/<int:pk>/delete/', employee_delete, name='employee_delete'),

    # API endpoints
    path('api/employees/', EmployeeListCreateAPI.as_view(), name='api_employees'),
    path('api/employees/<int:pk>/', employee_retrieve_delete_api, name='api_employee_detail'),
]
