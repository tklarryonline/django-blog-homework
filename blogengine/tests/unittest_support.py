from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils import timezone
from django.utils.text import slugify

from blogengine.models import Post, Category, Tag

def create_post(author, site, category,
                title='My first post',
                text='This is my first blog post'):
    return Post.objects.create(author=author,
                               site=site,
                               category=category,
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

def create_category(name='python',
                    description='The Python programming language'):
    return Category.objects.create(name=name, description=description)

def create_tag(name='perl',
               description='The Perl programming language'):
    return Tag.objects.create(name=name, description=description)

def create_test_post():
    # Create author
    author = create_user()
    # Create site
    site = create_site()
    # Create category
    category = create_category()
    # Create post
    return create_post(author=author, site=site, category=category)
