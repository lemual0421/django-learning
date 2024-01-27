from django.db import models

class BookLibrary(models.Model):
    title  = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=700, blank=True )
    preview = models.CharField(max_length=10000, blank=True )
    def __str__(self):
        return self.title