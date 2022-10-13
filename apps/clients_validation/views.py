from django.urls import reverse_lazy
from django.views import generic

from apps.clients_validation.forms import CustomUserCreationForm, \
    EditProfileForm


class SignUpView(generic.CreateView):
    template_name = "clients/signup.html"
    success_url = reverse_lazy("login")
    form_class = CustomUserCreationForm


class UserEditView(generic.UpdateView):
    template_name = "clients/edit_profile.html"
    success_url = reverse_lazy("clients:account_page")
    form_class = EditProfileForm

    def get_object(self, queryset=None):
        return self.request.user
