from django.urls import path
from blogging.admin import admin_site
from blogging.views import BlogListView, BlogDetailView

urlpatterns = [
    path("blog_admin/", admin_site.urls),
    path("", BlogListView().as_view(), name="blog_index"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
]
