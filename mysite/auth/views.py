from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import UserRegisterForm


class SignUpView(CreateView):
    template_name = "auth/register.html"
    success_url = reverse_lazy("auth:login")
    form_class = UserRegisterForm
