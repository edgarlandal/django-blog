from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.urls import reverse_lazy

from django.shortcuts import render

from .models import Posts


class PostsListView(ListView):
    template_name = "posts/list_post.html"
    model = Posts
    fields = "__all__"

    def get(self, request):
        posts = Posts.objects.all()
        context = {"posts": posts}
        return render(request, self.template_name, context)


class PostsCreateView(CreateView):
    template_name = "posts/create_post.html"
    model = Posts
    fields = "__all__"


class PostsDeleteView(DeleteView):
    template_name = "posts/delete_post.html"
    model = Posts
    fields = "__all__"
    success_url = reverse_lazy("list_post")


class PostsUpdateView(UpdateView):
    template_name = "posts/update_post.html"
    fields = ["title", "subtitle", "body"]
    model = Posts


class PostsDetailView(DetailView):
    template_name = "posts/detail_post.html"
    model = Posts
    context_object_name = 'post'
