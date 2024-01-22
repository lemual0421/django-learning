from django.db import models

class BookLibrary(models.Model):
    title  = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=700, blank=True )