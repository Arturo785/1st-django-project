from django.contrib import admin
from django.urls import path

from . import views


app_name = 'department_app' 


urlpatterns = [
    path('departamento_add/', views.NewDepartmentView.as_view(),name="crear_departamento"),
    path('list_all_departments/', views.ListAllDepartments.as_view(),name="listar_departamentos"),
    path('list_all_departments/<pk>', views.DepartmentDetailView.as_view(),name="detalle_departamentos"),
]