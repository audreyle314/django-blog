from django.urls import path
from blogging.admin import admin_site
from blogging.views import list_view, detail_view

urlpatterns = [
    path("blog_admin/", admin_site.urls),
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]