from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin
from app.movies.models import Movie
from app.series.models import Season


class Links(models.Model):
    thumbnail = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=160)
    slug_name = models.SlugField(max_length=350)
    description = models.TextField(null=True)
    url = models.URLField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Links, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Links, self).update(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Links, self).create(*args, **kwargs)

    class Meta:
        db_table = "links"
