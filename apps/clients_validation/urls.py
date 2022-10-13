from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.clients_validation import views
from apps.clients_validation.account_page_views import AccountPageView, \
    PasswordsChangeView

app_name = "clients"

urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
    path("edit_profile/", views.UserEditView.as_view(), name="edit_profile"),
    path("account_page/", login_required(AccountPageView.as_view()),
         name="account_page"),
    path("password/", login_required(PasswordsChangeView.as_view(template_name='clients/change_password.html')),
         name="password_change"),
]
