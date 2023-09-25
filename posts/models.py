from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Posts(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.title

    def get_absolute_url(self):
        reverse("detail_post", args=[self.pk])
