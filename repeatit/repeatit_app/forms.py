"""
Django form definition
"""

from django import forms


class CheckForm(forms.Form):
    """
    The form checks if a learner knows an answer written on a flashcard.
    """

    card_id = forms.IntegerField(required=True)
    can_recall = forms.BooleanField(required=False)
