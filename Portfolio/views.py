from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import *

class PortfolioViews(ListView):
    model = PortfolioModel
    template_name = 'Portfolio.html'
    context_object_name = 'member_list'

class PortfolioDetail(DetailView):
    model = PortfolioModel
    template_name = 'detail_page.html'
    context_object_name = 'post'   #id


class CreatePortfolio(CreateView):
    model = PortfolioModel
    template_name = 'portfolio_create.html'
    fields = ['full_name', 'age', 'nationality', 'info', 'image']
    success_url = reverse_lazy('Portfolio:views')


class DeletePortfolio(DeleteView):
    model = PortfolioModel
    template_name = 'delete_portfolio.html'
    context_object_name = 'delete_portfolio'
    success_url = reverse_lazy('Portfolio:views')

class EditPortfolio(UpdateView):
    model = PortfolioModel
    template_name = 'edit_portfolio.html'
    fields = ['full_name', 'age', 'nationality', 'info', 'image']
    success_url = reverse_lazy('Portfolio:views')
