from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib import admin


class Series(models.Model):
    thumbnail = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=160)
    slug_name = models.SlugField(max_length=350)
    description = models.TextField(null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Series, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Series, self).update(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Series, self).create(*args, **kwargs)

    class Meta:
        db_table = "series"


admin.site.register(Series)


class Season(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    thumbnail = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=160)
    slug_name = models.SlugField(max_length=350)
    description = models.TextField()
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Season, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Season, self).update(*args, **kwargs)

    def create(self, *args, **kwargs):
        self.slug_name = slugify(self.name + '-' + str(self.id))
        super(Season, self).create(*args, **kwargs)

    class Meta:
        db_table = "season"


admin.site.register(Season)
