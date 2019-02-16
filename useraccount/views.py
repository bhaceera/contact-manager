from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def home(request):
    return render(request, 'useraccount/index.html')


def reghome(request):
    return render(request, 'useraccount/register.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'User {username} has been created!')
            return redirect('reghome')
    else:
        form = UserRegisterForm()
    return render(request, 'useraccount/register.html', {'form': form})


# def handler404(request):
#     return render(request, '404.html', status=404)
#
# def handler500(request):
#     return render(request, '500.html', status=500)
