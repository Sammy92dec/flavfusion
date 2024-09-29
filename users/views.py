from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . import forms


def register(request):
  if request.method == "POST":
    form = forms.UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f"{username}, you're account has been created!")
        return redirect('home-flav')
  else:

   form = forms.UserRegisterForm()
  return render(request, 'register.html', {'form': form})


