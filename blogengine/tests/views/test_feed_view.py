import feedparser

from blogengine.models import Post
from blogengine.tests.acceptancetest_support import BaseAcceptanceTest
from blogengine.tests.unittest_support import create_tag
from blogengine.tests.unittest_support import create_test_post


class FeedViewTest(BaseAcceptanceTest):
    def set_up_post(self):
        # Set up post
        self.post = create_test_post()
        self.tag = create_tag()
        self.post.tags.add(self.tag)
        self.post.save()

    def test_all_post_feed(self):
        self.set_up_post()

        # Checks if we can find it
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, self.post)

        # Fetches the feed
        response = self.client.get('/feeds/posts/')
        self.assertEquals(response.status_code, 200)

        # Parses the feed
        feed = feedparser.parse(response.content)

        # Checks feed entries length
        self.assertEquals(len(feed.entries), 1)

        # Checks post received is the correct one
        feed_post = feed.entries[0]
        self.assertEquals(feed_post.title, self.post.title)
        self.assertEquals(feed_post.description, self.post.text)
