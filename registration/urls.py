from django.urls import path
from . import views

app_name='registration'

urlpatterns=[
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]

# <button type="submit"><a href="/signup">Sign Up</a></button>
#                     <button type="submit"><a href="/signin">Sign In</a></button>
