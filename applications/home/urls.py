from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [                         #indica que se trabaja con una vista generica
    path('home/', views.PruebaView.as_view()),
    path('lista/', views.TestListView.as_view()),
    path('add/', views.AddElementListView.as_view(), name="prueba_add"),
    path('resumen/', views.ResumenFundationView.as_view(), name="resumen_foundation"),
]