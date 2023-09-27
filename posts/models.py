from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Posts(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        reverse("detail_post", args=[self.id])
