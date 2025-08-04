from userauth.forms import CustomUserRegisterForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserRegisterForm
    template_name = 'userauth/sign_up.html'
    success_url = reverse_lazy('signin')
    success_message = "Account created successfully. You can now log in."
    login_url = 'signin'

    def form_valid(self, form):
        user = form.save()
        print('USER >>>', user)
        return super().form_valid(form)

class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'userauth/sign_in.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('issuedbooks_list')
    success_message = "Logged in successfully!"

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid Details, please try again !!')
        return super().form_invalid(form)

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('signin')
