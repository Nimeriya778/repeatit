"""
URL configuration to map URL paths to the application views
"""

from django.urls import path
from .views import FlashcardListView, FlashcardCreateView, FlashcardUpdateView, BoxView


urlpatterns = [
    path("", FlashcardListView.as_view(), name="flashcard-list"),
    path("new", FlashcardCreateView.as_view(), name="flashcard-create"),
    path("edit/<int:pk>", FlashcardUpdateView.as_view(), name="flashcard-update"),
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
]
