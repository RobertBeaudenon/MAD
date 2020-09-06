from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    concordia_id = models.IntegerField()
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'concordia_id']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
