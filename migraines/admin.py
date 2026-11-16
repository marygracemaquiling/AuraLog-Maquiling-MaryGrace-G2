from django.contrib import admin
from .models import Symptom, Trigger, MigraineLog

admin.site.register(Symptom)
admin.site.register(Trigger)
admin.site.register(MigraineLog)