"""
URL configuration to map URL paths to the application views
"""

from django.urls import path
from .views import FlashcardListView, FlashcardCreateView, FlashcardUpdateView


urlpatterns = [
    path("", FlashcardListView.as_view(), name="flashcard-list"),
    path("new", FlashcardCreateView.as_view(), name="flashcard-create"),
    path("edit/<int:pk>", FlashcardUpdateView.as_view(), name="flashcard-update"),
]
