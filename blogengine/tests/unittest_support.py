from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

from blogengine.models import Post

def create_post(author,
                title='My first post',
                text='This is my first blog post'):
    return Post.objects.create(author=author,
                               title=title,
                               text=text,
                               pub_date=timezone.now(),
                               slug=slugify(unicode(title)))

def create_user(username='testuser',
                email='user@example.com',
                password='password'):
    return User.objects.create_user(username, email, password)
