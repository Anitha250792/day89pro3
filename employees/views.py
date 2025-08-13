from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.decorators.http import require_http_methods
from .models import Employee

# --- CBVs ---
class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    ordering = ['-created_at']  # latest first

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'role', 'department', 'email']
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'role', 'department', 'email']
    success_url = reverse_lazy('employee_list')

# --- FBVs ---
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})

@require_http_methods(["GET", "POST"])
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer

# API (CBV): List + Create
class EmployeeListCreateAPI(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer

# API (FBV): Retrieve + Update + Delete
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def employee_retrieve_delete_api(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(EmployeeSerializer(employee).data)

    if request.method in ('PUT', 'PATCH'):
        partial = request.method == 'PATCH'
        ser = EmployeeSerializer(employee, data=request.data, partial=partial)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
