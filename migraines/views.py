from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.decorators import role_required
from .models import MigraineLog
from .forms import MigraineLogForm


@login_required
@role_required('patient')
def migraine_list(request):
    logs = MigraineLog.objects.filter(patient=request.user)
    return render(request, 'migraines/migraine_list.html', {'logs': logs})


@login_required
@role_required('patient')
def migraine_create(request):
    if request.method == 'POST':
        form = MigraineLogForm(request.POST)
        if form.is_valid():
            log = form.save(commit=False)
            log.patient = request.user
            log.save()
            form.save_m2m()
            messages.success(request, "Migraine episode logged successfully!")
            return redirect('migraine_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MigraineLogForm()
    return render(request, 'migraines/migraine_form.html', {'form': form, 'action': 'Log New'})


@login_required
@role_required('doctor')
def doctor_shared_logs(request):
    shared_logs = MigraineLog.objects.filter(is_shared_with_doctor=True).select_related('patient')
    return render(request, 'migraines/doctor_shared_logs.html', {'shared_logs': shared_logs})

    @login_required
@role_required('patient')
def migraine_update(request, pk):
    log = get_object_or_404(MigraineLog, pk=pk, patient=request.user)
    if request.method == 'POST':
        form = MigraineLogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            messages.success(request, "Migraine log updated successfully!")
            return redirect('migraine_list')
        else:
            messages.error(request, "Please fix the validation errors below.")
    else:
        form = MigraineLogForm(instance=log)
    return render(request, 'migraines/migraine_form.html', {'form': form, 'action': 'Edit'})


@login_required
@role_required('patient')
def migraine_delete(request, pk):
    log = get_object_or_404(MigraineLog, pk=pk, patient=request.user)
    if request.method == 'POST':
        log.delete()
        messages.success(request, "Migraine log deleted.")
        return redirect('migraine_list')
    return render(request, 'migraines/migraine_confirm_delete.html', {'log': log})