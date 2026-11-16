from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100, required=True)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'full_name', 'email', 'role']

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'age', 'contact_number', 'emergency_medical_contact', 'profile_photo']