from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog.html"


class BlogDetailedView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogEditView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class DeleteBlogView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("blog")