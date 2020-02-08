from django.db import models
from django.urls import reverse


class Library (models.Model):

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Library ")
        verbose_name_plural = ("Libraries")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # // i think you need to import reverse from somewhere
        return reverse("Library _detail", kwargs={"pk": self.pk})


