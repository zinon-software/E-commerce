from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('store')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# GCBV
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

