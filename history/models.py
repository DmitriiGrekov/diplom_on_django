from django.db import models


class History(models.Model):
    img1 = models.TextField()
    img2 = models.TextField()
    maintext = models.TextField()
    subtext = models.TextField()
    video = models.TextField()

    class Meta:
        verbose_name_plural = 'Истории'
        verbose_name = 'История'
