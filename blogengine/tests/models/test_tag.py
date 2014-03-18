from django.test import TestCase

from blogengine.models import Tag
from blogengine.tests.unittest_support import create_tag

class TagTest(TestCase):
    def test_create_tag(self):
        tag = create_tag()

        # Checks if we could find it
        all_tags = Tag.objects.all()
        self.assertEquals(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEquals(only_tag, tag)

        # Checks data
        self.assertEquals(only_tag.name, tag.name)
        self.assertEquals(only_tag.description, tag.description)
