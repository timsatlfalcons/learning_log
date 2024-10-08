from django.db import models

class Topic(models.Model):
    """A topic the user is learnng aobut."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

# Create your models here.
