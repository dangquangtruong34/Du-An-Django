from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save(commit=False)

            # hash password
            user.set_password(form.cleaned_data['password'])

            user.is_superuser = False
            user.is_staff = False

            user.save()
            return redirect('user_login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('user_login')

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('user_login')