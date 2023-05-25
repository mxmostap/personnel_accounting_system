from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView, PasswordResetView
from django.shortcuts import render, redirect
from django.views import View

from staff.forms import AuthorizationForm, UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'staff/home.html')

class MyLoginView(LoginView):
    template_name = 'staff/login.html'
    form_class = AuthorizationForm
    def form_invalid(self, form):
        messages.error(self.request, 'Неверные учетные данные.')
        return super().form_invalid(form)

class MyRegistrationView(View):
    template_name = 'staff/registration.html'
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def form_invalid(self, form):
        messages.error(self.request, 'Неверные данные для регистрации.')
        return super().form_invalid(form)

# class MyPasswordResetView(PasswordResetView):
#     template_name = 'staff/password_reset.html'
#     form_class = PasswordResetForm
#
#
#     def form_invalid(self, form):
#         messages.error(self.request, '.')
#         return super().form_invalid(form)