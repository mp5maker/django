from django.shortcuts import render

from django.views.generic import ListView, DetailView

from django.views.generic import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Article

from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(LoginRequiredMixin, ListView):
    template_name="articles/list.html"
    login_url=reverse_lazy('login')
    model=Article

class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name="articles/detail.html"
    login_url=reverse_lazy('login')
    model=Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name="articles/create.html"
    login_url=reverse_lazy('login')
    model=Article
    fields = ('title', 'body', )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name="articles/update.html"
    login_url=reverse_lazy('login')
    model=Article
    fields = ('title', 'body', )


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name="articles/delete.html"
    login_url=reverse_lazy('login')
    success_url=reverse_lazy("articles:list")
    model=Article