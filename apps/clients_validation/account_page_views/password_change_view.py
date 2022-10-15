from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from apps.clients_validation.forms import PasswordChangingForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("clients:password_success")
