from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *

class NewsViews(ListView):
    model = NewsModel
    template_name = 'news.html'
    context_object_name = 'news_list'

class NewsViewsDetail(DetailView):
    model = NewsModel
    template_name = 'news_detail.html'
    context_object_name = 'detail_news'   #id

class CreateNews(CreateView):
    model = NewsModel
    template_name = 'create.html'
    fields = ['image', 'title', 'news']
    success_url = reverse_lazy('News:NewsViews')

class DeleteNews(DeleteView):
    model = NewsModel
    template_name = 'delete_portfolio.html'
    context_object_name = 'delete_news'
    success_url = reverse_lazy('News:NewsViews')

class EditNews(UpdateView):
    model = NewsModel
    template_name = 'edit.html'
    fields = ['image', 'title', 'news']
    success_url = reverse_lazy('News:NewsViews')