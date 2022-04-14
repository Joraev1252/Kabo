from django.urls import path
from .views import *

app_name = 'Home'

urlpatterns = [
    path('', HomeViews.as_view(), name='HomeViews'),
    path('about/', AboutViews.as_view(), name='AboutViews'),
]
