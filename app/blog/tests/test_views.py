import pytest

from django.test import Client

from blog.models import Post


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()

    def test_post_detail_is_published(self, post_one):
        """Validation test:"""
        url = Post.get_absolute_url(post_one)

        res = self.client.get(url)

        assert res.status_code == 200

    def test_post_detail_is_draft(self, post_one):
        """Constraint Test:
        case:
            status: draft
        """
        post_one.status = Post.STATUS_CHOICES[0][0]
        post_one.save()

        url = Post.get_absolute_url(post_one)

        res = self.client.get(url)

        assert res.status_code == 404
