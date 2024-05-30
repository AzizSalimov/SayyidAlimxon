from django.db import models
from django.urls import reverse

from django.db import models
from django.core.validators import FileExtensionValidator


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='book_images/', null=False)  # Specify upload path
    follow_author = models.CharField(max_length=2083, blank=True)
    book_available = models.BooleanField(default=False)

    # Add the PDF field with appropriate validation
    pdf = models.FileField(upload_to='book_pdfs/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                           null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product


class Order(models.Model):
    prodict = models.ForeignKey
