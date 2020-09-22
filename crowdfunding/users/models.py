from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # required field = models.field()
    first_name = models.CharField(max_length=80, verbose_name ="First Name")
    last_name = models.CharField(max_length=80, verbose_name="Last Name")
    #image = models.URLField(max_length=200, verbose_name="Photo")
    email = models.CharField(max_length=100, verbose_name="Email")
    location = models.CharField(max_length=100,  verbose_name="Location")

    def full_name(self):
        return '%s %s' % self.first_name, self.last_name
