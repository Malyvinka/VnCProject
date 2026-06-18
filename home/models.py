from django.db import models

# Create your models here.
class Character(models.Model):
    SPECIES_CHOICES = [
        ('human', 'Human'),
        ('vampire', 'Vampire'),
        ('dhampir', 'Dhampir'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES, default='vampire')
    true_name = models.CharField(max_length=100, blank=True, null=True)
    malnomen = models.CharField(max_length=150, blank=True, null=True)
    is_corrupted = models.BooleanField(default=False)
    abilities = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
