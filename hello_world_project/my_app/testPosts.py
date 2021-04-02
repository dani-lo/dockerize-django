from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title")
        self.assertEqual(post.title, "My Title")