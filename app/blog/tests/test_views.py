import pytest
import requests

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from blog.models import Post

from api.v1.views.blog import PostList, PostDetail
from api.v1.serializers.blog import PostSerializer


POSTLIST_URL = reverse('post_list')


@pytest.mark.django_db
class TestPostList:
    def setup_method(self):
        self.client = APIClient()

    def test_list_anonymous(self, post_one):
        """ """
        res = self.client.get(POSTLIST_URL)

        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_list_logged(self, user_achille, post_one):
        """ """
        self.client.force_authenticate(user=user_achille)
        
        res = self.client.get(POSTLIST_URL)

        assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
class TestPostDetail:
    def setup_method(self):
        self.client = APIClient()

    def test_detail_anonymous(self, post_one):
        """ """
        POSTDETAIL_URL = reverse('post_detail', args=[post_one.id])

        res = self.client.get(POSTDETAIL_URL)

        assert res.status_code == status.HTTP_403_FORBIDDEN

    def test_detail_logged_id_ok(self, user_achille, post_one):
        """ """
        POSTDETAIL_URL = reverse('post_detail', args=[post_one.id])
        self.client.force_authenticate(user=user_achille)

        res = self.client.get(POSTDETAIL_URL)

        assert res.status_code == status.HTTP_200_OK

    def test_detail_logged_id_ko(self, user_achille, post_one):
        """ """
        POSTDETAIL_URL = reverse('post_detail', args=[456])

        self.client.force_authenticate(user=user_achille)
        res = self.client.get(POSTDETAIL_URL)

        assert res.status_code == status.HTTP_404_NOT_FOUND
