from django.db import models
import random

class ChoiceManager(models.Manager):
    def pick(self, key):
        candidates = self.filter(key=key)
        if len(candidates) == 0:
            raise Exception("There are no records with this key.")
        weight_sum = sum([candidate.weight for candidate in candidates])
        random_index = random.randint(1, weight_sum)
        current = 0
        for candidate in candidates:
            current += candidate.weight
            if current >= random_index:
                return candidate
