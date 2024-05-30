from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostList, PostDetail, CommentList, CommentDetail, CategoryList, CategoryDetail, PostListCreateView

urlpatterns = [
    path("posts/", PostList.as_view(), name='blog_posts'),
    path("posts/<int:pk>/", PostDetail.as_view()),
    path("comments/", CommentList.as_view(), name = 'blog_comments'),
    path('comments/<int:pk>/', CommentDetail.as_view()),

    path('categories/', CategoryList.as_view(), name = 'category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view()),

    path('postss/', PostListCreateView.as_view(), name = 'Post'),
    path("postss/<int:pk>/", PostListCreateView.as_view())


]

urlpatterns = format_suffix_patterns(urlpatterns)
