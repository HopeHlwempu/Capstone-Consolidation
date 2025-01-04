"""
urls.py

Defines URL patterns for the user authentication application.
Maps URLs to corresponding view functions for user registration, login, logout, authentication, and profile details.
"""

from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('register/', views.register, name='register'),
    # Maps to the user registration view.
    path('login/', views.user_login, name='login'),
    # Maps to the login page view.
    path('logout/', views.user_logout, name='logout'),
    # Maps to the logout view to end the user session.
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    # Maps to the authentication view for validating user credentials.
    path('user_details/', views.show_user, name='show_user'),
    # Maps to the view for displaying user profile details.
]
