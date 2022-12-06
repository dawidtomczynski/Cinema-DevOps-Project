from django.db import models
from django.template.defaultfilters import slugify
from djongo import models as m


class Movie(models.Model):
    _id = m.ObjectIdField()
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
