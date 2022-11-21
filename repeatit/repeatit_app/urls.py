"""
URL configuration to map URL paths to the application views
"""

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import FlashcardListView, FlashcardCreateView, FlashcardUpdateView, BoxView


urlpatterns = [
    path("", FlashcardListView.as_view(), name="flashcard-list"),
    path("new", FlashcardCreateView.as_view(), name="flashcard-create"),
    path("edit/<int:pk>", FlashcardUpdateView.as_view(), name="flashcard-update"),
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
    path("accounts/login", auth_views.LoginView.as_view(template_name='repeatit_app/login.html'))
]
