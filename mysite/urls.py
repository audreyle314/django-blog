from django.contrib import admin
from blogging.admin import admin_site
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path('polling/', include('polling.urls')),
    path('', include('blogging.urls')),
    path('blog_admin/', admin_site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
]