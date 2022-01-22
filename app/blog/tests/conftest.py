import pytest

from blog.models import Post


@pytest.fixture
def user_achille(django_user_model):
    achille = django_user_model.objects.create_user(
        username="achille",
        password="test123",
    )
    achille.save()

    return achille


@pytest.fixture
def post_one(user_achille):
    post = Post.objects.create(
        title="Another post",
        slug="another-post",
        body="Post body.",
        author=user_achille,
        status="published",
    )
    post.save()

    return post
