# The above class defines a Django model for a project in a portfolio, with fields for title,
# description, image, URL, and date.
from django.db import models

from django.db import models
from django.db.models.fields import CharField, DateField, URLField
from django.db.models.fields.files import ImageField
from datetime import date


class Project(models.Model):
    app_label = 'portfolio'
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to="portfolio/images")
    url = URLField(blank=True)
    date = DateField(default=date.today)

    def __str__(self) -> str:
        return self.title
