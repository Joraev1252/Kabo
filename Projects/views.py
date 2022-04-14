from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

class ProjectDetail(DetailView):
    model = ProjectModel
    template_name = 'detail_project.html'
    context_object_name = 'post'   #id

class ProjectViews(ListView):
    model = ProjectModel
    template_name = 'projects.html'
    context_object_name = 'project_list'

class Projectadd(CreateView):
    model = ProjectModel
    template_name = 'add.html'
    context_object_name = 'add_project'
    success_url = reverse_lazy('projects:views')
    fields = ['company', 'founder', 'info', 'image']


class DeleteProject(DeleteView):
    model = ProjectModel
    template_name = 'delete_project.html'
    context_object_name = 'delete_news'
    success_url = reverse_lazy('projects:views')

class EditProject(UpdateView):
    model = ProjectModel
    template_name = 'edit.html'
    fields = ['company', 'founder', 'info', 'image']
    success_url = reverse_lazy('projects:views')
