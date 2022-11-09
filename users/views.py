from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from categories.models import Category


def register(request):
    user_admin = User.objects.get(username='admin')
    def_cat = Category.objects.filter(user=user_admin)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            # new_user = User.objects.create_user(username=username)
            # new_user.save()
            # login(request, new_user)
            # for i in def_cat:
            #     Category.objects.create(name=i.name, user=new_user).save() #TODO add base category
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/register.html')
