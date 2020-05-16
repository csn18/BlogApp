from django.db import models


class UserDate(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
