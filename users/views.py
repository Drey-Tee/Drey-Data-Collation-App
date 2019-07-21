from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
from file_logs.models import UploadFile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('app_home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    file_list = UploadFile.objects.filter(user=request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(file_list, 10)
    try:
        files = paginator.page(page)
    except PageNotAnInteger:
        files = paginator.page(1)
    except EmptyPage:
        files = paginator.page(paginator.num_pages)

    return render(request, 'users/profile.html', { 'files': files })
