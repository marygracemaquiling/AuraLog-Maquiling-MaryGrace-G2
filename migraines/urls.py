from django.urls import path
from . import views

urlpatterns = [
    path('', views.migraine_list, name='migraine_list'),
    path('new/', views.migraine_create, name='migraine_create'),
    path('shared-records/', views.doctor_shared_logs, name='doctor_shared_logs'),
]