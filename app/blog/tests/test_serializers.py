import pytest

from rest_framework.test import APIClient

from api.v1.serializers.blog import PostSerializer


@pytest.mark.django_db
class TestPostSerializer:
    def setup_method(self):
        self.client = APIClient()

    def test_serializer_data(self, post_one):
        """Validation test:"""
        res = PostSerializer(instance=post_one)

        assert res.data["id"] == 2
        assert res.data["title"] == "Another post"
