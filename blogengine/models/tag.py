from django.db import models
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=40, unique=True, blank=True, null=True)

    class Meta:
        app_label = "blogengine"
        ordering = ["name"]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/tag/%s/" % self.slug

    def save(self, force_insert=False, force_update=False, using=None):
        if not self.slug:
            self.slug = slugify(unicode(self.name))
        super(Tag, self).save()
