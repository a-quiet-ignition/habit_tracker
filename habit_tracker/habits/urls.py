from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import dashboard


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='habits/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='habits/logout.html'), name='logout'),
    path('habits/', views.HabitListView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', views.HabitDetailView.as_view(), name='habit_detail'),
    path('habit/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habit/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('habit/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit_delete'),
    path('habit/<int:habit_pk>/log/create/', views.HabitLogCreateView.as_view(), name='habitlog_create'),
    path('habitlogs/', views.HabitLogListView.as_view(), name='habitlog_list'),
    path('habitlog/<int:pk>/', views.HabitLogDetailView.as_view(), name='habitlog_detail'),
    path('habitlog/<int:pk>/update/', views.HabitLogUpdateView.as_view(), name='habitlog_update'),
    path('habitlog/<int:pk>/delete/', views.HabitLogDeleteView.as_view(), name='habitlog_delete'),
    path('dashboard/', dashboard, name='dashboard'),
]