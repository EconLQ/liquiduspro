from django.urls import path

from apps.clients_validation import views

app_name = "clients"

urlpatterns = [
    path("", views.SignUpView.as_view(), name="signup"),
    path("edit_profile/", views.UserEditView.as_view(), name="edit_profile"),
    path("account_page/", views.AccountPageView.as_view(), name="account_page"),
]
