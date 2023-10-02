from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Posts, Status
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostsCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/create_post.html"
    model = Posts
    fields = ["title", "author", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance_author = self.request.user
        return super().form_valid(form)


class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/update_post.html"
    model = Posts
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete_post.html"
    model = Posts
    success_url = reverse_lazy("list_post")

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostListView(ListView):
    template_name = "posts/list_post.html"
    model = Posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published = Status.objects.get(name="published")
        context["posts_list"] = (
            Posts.objects.filter(status=published).order_by("created_on").reverse()
        )
        print(context)
        return context


class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list_post.html"
    model = Posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="draft")
        context["post_list"] = (
            Posts.objects.filter(status=draft)
            .filter(author=self.request.user)
            .order_by("created_on")
            .reverse()
        )
        return context


class PostsDetailView(DetailView):
    template_name = "posts/detail_post.html"
    model = Posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft = Status.objects.get(name="draft")

        if (
            context["posts"].status == draft
            and context["posts"].author != self.request.user
        ):
        
            context["posts"] = None
        if context["posts"]:
            return context
        return context
