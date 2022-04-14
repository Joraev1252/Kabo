from django.urls import path
from .views import *

app_name = 'Portfolio'

urlpatterns = [
    path('', PortfolioViews.as_view(), name='views'),
    path('delete/<int:pk>', DeletePortfolio.as_view(), name='delete'),
    path('create/', CreatePortfolio.as_view(), name='create'),
    path('update/<int:pk>', EditPortfolio.as_view(), name='edit'),
    path('<int:pk>', PortfolioDetail.as_view(), name='detail'),
]