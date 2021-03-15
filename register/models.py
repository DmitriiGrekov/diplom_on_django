from django.db import models
from django.conf import settings


class Yourmodel(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    about = models.TextField()
    country = models.CharField(max_length=100)
    img = models.TextField()

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    class Meta:
        verbose_name_plural = 'Профили'
        verbose_name = 'Профиль'
