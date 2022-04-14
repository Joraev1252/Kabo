from django.urls import path
from .views import *

app_name = 'News'

urlpatterns = [
    path('', NewsViews.as_view(), name='NewsViews'),
    path('edit/<int:pk>', EditNews.as_view(), name='edit'),
    path('<int:pk>', NewsViewsDetail.as_view(), name='NewsDetail'),
    path('create/', CreateNews.as_view(), name='CreateViews'),
    path('delete/<int:pk>', DeleteNews.as_view(), name='delete'),
]