from django.contrib.auth.models import User
from django.views import generic


class AccountPageView(generic.ListView):
    model = User
    template_name = "clients/account_page.html"
