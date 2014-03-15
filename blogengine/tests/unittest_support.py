from django.utils import timezone
from django.utils.text import slugify

from blogengine.models import Post

def create_post(title='My first post',
                text='This is my first blog post'):
    return Post.objects.create(title=title,
                               text=text,
                               pub_date=timezone.now(),
                               slug=slugify(unicode(title)))
