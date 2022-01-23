from django.urls import path
from api.v1.views.blog import PostList, PostDetail


urlpatterns = [
    path('blog/', PostList.as_view(), name="post_list"),
    path('blog/<int:pk>/', PostDetail.as_view(), name="post_detail"),
]