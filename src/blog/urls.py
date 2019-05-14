from django.urls import path, re_path

from .views import (
    blog_post_detail_page,
    blog_post_list_view,
    blog_post_create_view,
    blog_post_update_view,
    blog_post_delete_view,
)

urlpatterns = [
    path('blogs', blog_post_list_view),
    path('blogs/<str:slug>/', blog_post_detail_page),
    path('blogs/<str:slug>/edit/', blog_post_update_view),
    path('blogs/<str:slug>/delete/', blog_post_delete_view),
    path('blogs-new/', blog_post_create_view),
    re_path(r'^blog-regex/(?P<id>\d+)/$', blog_post_detail_page)
]
