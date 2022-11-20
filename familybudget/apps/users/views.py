from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView

from apps.users.forms import CustomUserCreationForm


class RegisterView(SuccessMessageMixin, UserPassesTestMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")
    success_message = _("Account was created successfully.")

    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("home"))
