from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'registration/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, 'Your account has been successfully created.')

        return redirect('registration:signin')


    return render(request, 'registration/signup.html')


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('Home:HomeViews')
            # return render(request, 'Home:HomeViews')

        else:
            messages.error(request, "Your account was not found.")
            return redirect('registration:home')

    return render(request, 'registration/signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли.')
    return redirect('registration:home')