from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Habit, HabitLog
from .forms import HabitForm, CustomUserForm

# Create your views here.

# User Sign Up View
class SignUpView(CreateView):
    form_class = CustomUserForm
    template_name = 'habits/register.html'
    success_url = reverse_lazy('login')
    
    

# Habit Views
class HabitListView(ListView):
    model = Habit
    template_name = 'habits/habit_list.html'
    context_object_name = 'habits'

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
    
class HabitDetailView(DetailView):
    model = Habit
    template_name = 'habits/habit_detail.html'
    context_object_name = 'habit'
    
    
class HabitCreateView(CreateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habits/habit_form.html'
    success_url = reverse_lazy('habit_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'habits/habit_form.html'
    success_url = reverse_lazy('habit_list')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
class HabitDeleteView(LoginRequiredMixin, DeleteView):
    model = Habit
    template_name = 'habits/habit_confirm_delete.html'
    success_url = reverse_lazy('habit_list')

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)