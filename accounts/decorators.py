from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def role_required(allowed_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.role != allowed_role:
                messages.error(request, "Access denied: You do not have permission to view that dashboard.")
                return redirect('patient_dashboard' if request.user.role == 'patient' else 'doctor_dashboard')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator