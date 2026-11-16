from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, ProfileUpdateForm
from .decorators import role_required

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_redirect')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_redirect')
    if request.method == 'POST':
        email = request.POST.get('email', '').lower()
        password = request.POST.get('password', '')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.full_name}!")
            return redirect('dashboard_redirect')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'accounts/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required
def dashboard_redirect(request):
    if request.user.role == 'doctor':
        return redirect('doctor_dashboard')
    return redirect('patient_dashboard')

@login_required
@role_required('patient')
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
@role_required('doctor')
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')

@login_required
def profile_view(request):
    # Enforces BR-04: request.user ensures users only view/edit their own profile
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('profile')
        else:
            messages.error(request, "Failed to update profile. Please check your inputs.")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})