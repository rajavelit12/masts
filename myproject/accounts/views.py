from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            UserProfile.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                gender=form.cleaned_data['gender'],
                dob=form.cleaned_data['dob']
            )
            return redirect('register')  # or home page
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
