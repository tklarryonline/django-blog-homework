from django.test import TestCase

from blogengine.models import Category
from blogengine.tests.unittest_support import create_category

class CategoryTest(TestCase):
    def test_create_category(self):
        category = create_category()

        # Checks if we could find it
        all_categories = Category.objects.all()
        self.assertEquals(len(all_categories), 1)
        only_category = all_categories[0]
        self.assertEquals(only_category, category)

        # Checks data
        self.assertEquals(only_category.name, category.name)
        self.assertEquals(only_category.description, category.description)
