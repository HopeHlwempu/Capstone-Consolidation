"""
urls.py

This module defines URL patterns for the polls application.
Each pattern maps a specific URL to its corresponding view function.
"""

from django.urls import path
from . import views  # Import view functions from views.py

app_name = 'polls'  # Namespace for polls application

urlpatterns = [
    path('', views.index, name='index'),
    # URL pattern for the home page of the polls app. Displays a list of the latest questions.

    path('<int:question_id>/', views.detail, name='detail'),
    # URL pattern for viewing the details of a specific poll question.
    # Captures an integer question_id to fetch the question details.

    path('<int:question_id>/results/', views.results, name='results'),
    # URL pattern for viewing the results of a specific poll question.
    # Captures an integer question_id to fetch the question's results.

    path('<int:question_id>/vote/', views.vote, name='vote'),
    # URL pattern for submitting a vote for a specific poll question.
    # Captures an integer question_id to handle the voting logic.
]