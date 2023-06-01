from django.contrib import admin
from blogging.models import Post, Category


# this is the admin interface that gives us the ability to tag a post
# with a category from the post page.
class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    # raw_id_fields = ["categories"]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    exclude = ["posts"]


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


class MyAdminSite(admin.AdminSite):
    site_header = "My Blog"


admin_site = MyAdminSite(name="blog_admin")

admin_site.register(Post, PostAdmin)

admin_site.register(Category, CategoryAdmin)
