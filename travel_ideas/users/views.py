from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Created new account: {user.username}')
            return redirect('/')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
                print(request, error)
    else:
        form = UserRegistrationForm()

    return render(
        request,
        "users/registration.html",
        context={'form': form}
    )