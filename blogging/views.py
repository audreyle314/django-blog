from blogging.models import Post
from django.shortcuts import render
from django.views.generic.detail import DetailView


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
