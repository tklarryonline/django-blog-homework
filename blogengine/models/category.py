from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        app_label = "blogengine"
        ordering = ["name"]
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name
