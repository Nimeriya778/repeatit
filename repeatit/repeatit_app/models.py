"""
The model defines how the db tables looks.
"""

from django.db import models

# A box means a repetition interval
NUM_BOXES = 3
BOXES = range(1, NUM_BOXES + 1)


class Flashcard(models.Model):
    """
    A flashcard has a question on one side and an answer on the other.
    """

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question)

    def move(self, can_recall):
        """
        If a learner can recall the solution written on a flashcard,
        then the flashcard moves to the next box.
        Otherwise, the flashcard moves to the first box.
        """

        if can_recall:
            group = self.box + 1
        else:
            group = BOXES[0]

        if group in BOXES:
            self.box = group
            self.save()
        return self
