
from django.db import models
from .library import Library
from .librarian import Librarian
from django.urls import reverse


class Book (models.Model):

    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    author = models.CharField( max_length=50)
    pub_year = models.CharField( max_length=50)
    location = models.ForeignKey(Library, on_delete=models.CASCADE)
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # import reverse?
        # for some reason reverse is undefined
        return reverse("Book_detail", kwargs={"pk": self.pk})
