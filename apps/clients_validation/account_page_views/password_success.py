from django.shortcuts import render


def password_success(request):
    return render(request, "clients/password_success.html", {})
