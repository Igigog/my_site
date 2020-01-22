from django.db import models
from django.contrib.auth.models import User


class Thread(models.Model):
    title = models.CharField(max_length=80, default='')
    text = models.CharField(max_length=400, default='')
    pub_date = models.DateTimeField('date published')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.title


class Message(models.Model):
    text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
