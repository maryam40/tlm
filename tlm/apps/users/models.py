from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    """
    Custom `User` model.

    With this custom user model we are able to further customize the `User`
    model in the future if the need arises.
    https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """

    # First Name and Last Name do not cover name patterns around the globe.
    full_name = models.CharField(_('Full Name'), max_length=255, blank=True, null=True)
