from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='habits/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='habits/logout.html'), name='logout'),
    path('habits/', views.HabitListView.as_view(), name='habit_list'),
    path('habits/<int:pk>/', views.HabitDetailView.as_view(), name='habit_detail'),
    path('habits/create/', views.HabitCreateView.as_view(), name='habit_create'),
    path('habits/<int:pk>/update/', views.HabitUpdateView.as_view(), name='habit_update'),
    path('habits/<int:pk>/delete/', views.HabitDeleteView.as_view(), name='habit_delete'),
]