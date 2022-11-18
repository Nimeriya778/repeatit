"""
Web pages description
"""

from typing import Any
import random
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.db.models import QuerySet
from .models import Flashcard
from .forms import CheckForm


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


class BoxView(FlashcardListView):
    """
    The webpage displays only the flashcards from the current box.
    """

    # pylint:disable=no-member, unused-argument

    template_name = "repeatit_app/box.html"
    form_class = CheckForm

    def get_queryset(self) -> QuerySet:

        return Flashcard.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs) -> dict[str, Any]:

        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]

        if self.object_list:
            context["check_card"] = random.choice(self.object_list)

        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """
        Process incoming POST requests.
        """

        form = self.form_class(request.POST)

        if form.is_valid():
            card = get_object_or_404(Flashcard, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["can_recall"])

        refer = request.META.get("HTTP_REFERER")
        if refer is None:
            refer = reverse_lazy("flashcard-list")

        return redirect(refer)
