from django.urls import path, include

import blogging.views
from blogging.admin import admin_site
from blogging.views import BlogListView, BlogDetailView, homepage, PostViewSet, CategoryViewSet
from rest_framework import routers

# app_name = 'blogging'

router = routers.DefaultRouter()
# router.register(r'users', blogging.views.UserViewSet)
router.register(r'posts', blogging.views.PostViewSet)
router.register(r'categories', blogging.views.CategoryViewSet)

urlpatterns = [
    path('', BlogListView().as_view(), name="blog_index"),
    path('blog_admin/', admin_site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path('add/', homepage, name="add_post"),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
]