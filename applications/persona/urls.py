from django.contrib import admin
from django.urls import path


from . import views

app_name = 'persona_app'  #el wrapper de las urls de aqui

urlpatterns = [                         #indica que se trabaja con una vista generica
    path('', views.HomeView.as_view(), name="inicio"),    
    path('all_employes/', views.listAllEmployes.as_view(), name="listAllEmployees"),    
    path('edit_all_employes/', views.EditAllEmployees.as_view(), name="EditAllEmployees"),    
    path('all_employes_department/<name>/', views.listEmployesByArea.as_view(), name= "list_employees_by_area"),    
    path('all_employes_job/<job>/', views.listEmployesByJob.as_view()),    
    path('all_employes_kword/', views.listEmployesBykword.as_view()),    
    path('all_employes_habilities/', views.listEmployesByHabilities.as_view()),    
    path('detail_employes/<pk>', views.EmployeDetailView.as_view(), name= "detail_of_employee"),    
    path('create-employe/', views.EmployeCreateView.as_view(), name="CreateEmployee"),    
    path('success/', views.SucessViewRegistration.as_view(), name='correcto'),    
    path('update-employe/<pk>', views.UpdateEmployeView.as_view(), name='update_employe'),    
    path('delete-employe/<pk>', views.DeleteEmployeView.as_view(), name='delete_employe'),    
]