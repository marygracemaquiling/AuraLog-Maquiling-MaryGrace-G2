from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('profile/', views.profile_view, name='profile'),
]