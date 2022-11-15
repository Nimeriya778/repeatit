"""
Web pages description
"""

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Flashcard


class FlashcardListView(ListView):
    """
    The app homepage shows all cards in boxes.
    """

    model = Flashcard
    queryset = Flashcard.objects.all()  # pylint:disable=no-member


class FlashcardCreateView(CreateView):
    """
    The webpage displays a form for creating a new flashcard.
    After the form is filled out and submitted, the browser sends POST request,
    and the view processes the data and then redirects to the same url.
    """

    model = Flashcard
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("flashcard-create")


class FlashcardUpdateView(UpdateView):
    """
    The form for editing an existing flashcard.
    After the form is filled out and submitted, the redirects to the homepage.
    """

    model = Flashcard
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("flashcard-list")
