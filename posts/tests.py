from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="test123",
            email="test123@email.com",
            password="testpass123",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            title="test post",
            body="lorem ipsum lorem ipsum lorem ipsum lorem ipsum",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "test123")
        self.assertEqual(self.post.title, "test post")
        self.assertEqual(
            self.post.body, "lorem ipsum lorem ipsum lorem ipsum lorem ipsum"
        )
        self.assertEqual(str(self.post), "test post")
