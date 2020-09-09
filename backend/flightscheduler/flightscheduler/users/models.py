from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class CustomUser(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    concordia_id = models.IntegerField()
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'concordia_id']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    # Create token for user who just registered
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            # print(sender)
            # print(instance)
            Token.objects.create(user=instance)
            # print(token)


