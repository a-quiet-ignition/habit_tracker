from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Habit, HabitLog


# User Form
User = get_user_model()

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

#Habit Form
class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Habit.objects.filter(name=name).exists():
            raise forms.ValidationError("Habit with this name already exists.")
        return name
    

# Habit Log Form
class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ['habit', 'date', 'completed']
        widgets = {
            'habit': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        habit = cleaned_data.get('habit')
        date = cleaned_data.get('date')
        
        if HabitLog.objects.filter(habit=habit, date=date).exists():
            raise forms.ValidationError("A log for this habit on this date already exists.")
        
        return cleaned_data
    
    