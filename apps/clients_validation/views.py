from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserChangeForm

from apps.clients_validation.forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    template_name = "clients/signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm


class UserEditView(generic.UpdateView):
    template_name = "clients/edit_profile.html"
    success_url = reverse_lazy("clients:account_page")
    form_class = UserChangeForm

    def get_object(self, queryset=None):
        return self.request.user


class AccountPageView(generic.ListView):
    model = User
    template_name = "clients/account_page.html"
