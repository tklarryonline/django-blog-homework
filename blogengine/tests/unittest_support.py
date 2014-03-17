from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils import timezone
from django.utils.text import slugify

from blogengine.models import Post

def create_post(author, site,
                title='My first post',
                text='This is my first blog post'):
    return Post.objects.create(author=author,
                               site=site,
                               title=title,
                               text=text,
                               pub_date=timezone.now(),
                               slug=slugify(unicode(title)))

def create_user(username='testuser',
                email='user@example.com',
                password='password'):
    return User.objects.create_user(username, email, password)

def create_site(name='example.com', domain='example.com'):
    return Site.objects.create(name=name, domain=domain)
