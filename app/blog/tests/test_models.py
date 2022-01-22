import pytest

from blog.models import Post


@pytest.mark.django_db
class TestModels:
    def test_str(self, post_one):
        """Validation test:"""
        post = Post.objects.get(title=post_one.title)

        assert str(post) == post_one.title
