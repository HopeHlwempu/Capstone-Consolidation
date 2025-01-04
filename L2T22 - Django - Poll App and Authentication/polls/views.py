"""
views.py

This module contains view functions for the polls application.
Each view handles HTTP requests for listing polls, viewing poll details,
voting on choices, and displaying results.
"""

from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def index(request):
    """Display a list of available polls."""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    """Show poll details with choices."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    """Submit a vote for a poll choice."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to results page after POST to prevent double submission.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    """Display poll results."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required
def index(request):
    """
    Display the latest five poll questions.

    Fetches the latest five questions ordered by publication date in descending order
    and renders them on the 'polls/poll.html' template.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with the latest questions.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/poll.html', context)


@login_required
def detail(request, question_id):
    """
    Display the details of a specific poll question.

    Fetches a question by its ID and renders it on the 'polls/detail.html' template.

    Args:
        request: The HTTP request object.
        question_id (int): The ID of the question to display.

    Returns:
        HttpResponse: The rendered HTML page with question details.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def results(request, question_id):
    """
    Display the results of a specific poll question.

    Fetches a question by its ID along with its choices and renders it on the
    'polls/results.html' template.

    Args:
        request: The HTTP request object.
        question_id (int): The ID of the question for which to display results.

    Returns:
        HttpResponse: The rendered HTML page with question results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


@login_required
def vote(request, question_id):
    """
    Handle voting for a specific poll question.

    Processes the user's vote for a selected choice, increments the vote count,
    and saves it. If no choice is selected, redisplays the voting form with an error message.

    Args:
        request: The HTTP request object containing POST data.
        question_id (int): The ID of the question being voted on.

    Returns:
        HttpResponseRedirect: Redirects to the results page after successful voting.
        HttpResponse: Redisplays the voting form with an error message if no choice is selected.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

