from django import forms
from django.utils import timezone
from .models import MigraineLog, Symptom, Trigger


class MigraineLogForm(forms.ModelForm):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    triggers = forms.ModelMultipleChoiceField(
        queryset=Trigger.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = MigraineLog
        fields = [
            'start_time',
            'end_time',
            'severity_score',
            'symptoms',
            'triggers',
            'medication_taken',
            'notes',
            'is_shared_with_doctor',
        ]
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'severity_score': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-input'}),
            'medication_taken': forms.TextInput(attrs={'placeholder': 'e.g., Ibuprofen 400mg, Sumatriptan', 'class': 'form-input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describe pain location, aura duration, or relief measures...', 'class': 'form-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        severity = cleaned_data.get('severity_score')

        if start_time and start_time > timezone.now():
            self.add_error('start_time', "Attack start time cannot be in the future.")

        if start_time and end_time and end_time < start_time:
            self.add_error('end_time', "End time cannot be earlier than the start time.")

        if severity is not None and (severity < 1 or severity > 10):
            self.add_error('severity_score', "Severity score must be between 1 and 10.")

        return cleaned_data