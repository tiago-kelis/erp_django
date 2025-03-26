from django.urls import path
from companies.views.employee import Employees, EmployeeDetail

urlpatterns = [

    # Employees EndPoints
    path('employees', Employees.as_view()),
    path('employees/<int:employee_id>', EmployeeDetail.as_view()),
]