from django.db import models

class DNASequence(models.Model):
    dna = models.TextField()
    is_mutant = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)