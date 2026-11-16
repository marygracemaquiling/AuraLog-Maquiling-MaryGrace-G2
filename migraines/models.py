from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Symptom(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Trigger(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MigraineLog(models.Model):
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='migraine_logs'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    severity_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Pain severity from 1 (mild) to 10 (severe)"
    )
    symptoms = models.ManyToManyField(Symptom, blank=True, related_name='migraine_logs')
    triggers = models.ManyToManyField(Trigger, blank=True, related_name='migraine_logs')
    medication_taken = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    is_shared_with_doctor = models.BooleanField(
        default=True,
        help_text="Allow healthcare providers to view this episode in clinical reviews"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return f"{self.patient.full_name} - {self.start_time.strftime('%Y-%m-%d %H:%M')} (Severity: {self.severity_score}/10)"

    @property
    def duration_hours(self):
        if self.end_time and self.start_time:
            diff = self.end_time - self.start_time
            return round(diff.total_seconds() / 3600, 1)
        return None