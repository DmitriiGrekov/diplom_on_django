from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=120)
    shortdescription = models.TextField(max_length=120)
    description = models.TextField()
    mainimg = models.TextField()
    img1 = models.TextField()
    img2 = models.TextField()
    img3 = models.TextField()
    img4 = models.TextField()
    img5 = models.TextField()
    img6 = models.TextField()
    videp = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Игроки'
        verbose_name = 'Игрок'


class Comment(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    comment_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.comment_name

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Коммент'
