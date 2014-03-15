from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        app_label = "blogengine"
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)
