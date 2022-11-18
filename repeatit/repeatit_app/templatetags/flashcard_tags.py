"""
Custom template tag registration
"""

from django import template
from repeatit_app.models import BOXES, Flashcard


register = template.Library()


@register.inclusion_tag("repeatit_app/box_links.html")
def boxes_as_links() -> dict:
    """
    Return the context which is used in the 'box_links.html' template.
    """

    # pylint:disable=no-member

    boxes = []

    for box_num in BOXES:
        card_count = Flashcard.objects.filter(box=box_num).count()
        boxes.append(
            {
                "number": box_num,
                "card_count": card_count,
            }
        )

    return {"boxes": boxes}
