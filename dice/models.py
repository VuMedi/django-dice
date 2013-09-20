from django.db import models
from dice.managers import ChoiceManager


class ChoiceModel(models.Model):
    """
    An abstract base class model that provides field for random weighted selection.
    """
    key = models.CharField(max_length=255, blank=False, null=False)
    weight = models.IntegerField(default=1)

    objects = ChoiceManager()

    class Meta:
        abstract = True
