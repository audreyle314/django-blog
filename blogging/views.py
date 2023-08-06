from blogging.models import User, Post, Category
from blogging.forms import PostForm
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from rest_framework import permissions

from blogging.serializers import PostSerializer, CategorySerializer


class ListView():
    def as_view(self):
        return self.get

    def get(self, request):
        model_list_name = self.model.__name__.lower() + '_list'
        # the exclude method will not display another post I created called 'test exclude'
        # because it doesn't have a published date.
        queryset = Post.objects.order_by('-published_date').exclude(published_date__exact=None)
        context = {model_list_name: queryset}
        return render(request, self.template_name, context)


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def post(self, request, *args, **kwargs):
        blog_post = self.get_object()
        context = {'object': blog_post}
        return render(request, 'blogging/detail.html', context)


# class AddModel(DetailView):
#     model = Post
#     template_name = 'blogging/detail.html'


def homepage(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Your post was successfully added!')
        else:
            messages.error(request, 'Error saving form')

        return redirect("blogging:homepage")
    post_form = PostForm()
    posts = Post.objects.all()
    return render(request=request, template_name="blogging/add.html",
                  context={'post_form': post_form, 'posts': posts})


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#
#     queryset = User.objects.all().order_by("-date_joined")
#     serializer_class = UserSerializer
#     lookup_field = "username"
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    queryset = Post.objects.all().order_by("-published_date")
    serializer_class = PostSerializer
    lookup_field = "title"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     username = self.kwargs["author"]
    #     user_posts = get_object_or_404(User, username=username)
    #     return user_posts.objects.all().order_by("-published_date")


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
