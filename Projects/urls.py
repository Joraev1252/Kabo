from django.urls import path
from .views import *

app_name = 'projects'

urlpatterns = [
    path('', ProjectViews.as_view(), name='views'),
    path('create/', Projectadd.as_view(), name='add'),
    path('<int:pk>', ProjectDetail.as_view(), name='detail'),
    path('edit/<int:pk>', EditProject.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteProject.as_view(), name='delete')
]