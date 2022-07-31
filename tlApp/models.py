from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField("Post content")
    userPost = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Post by", default="")
    postDate = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('postDetails', args=[self.pk])

    class Meta:
        verbose_name_plural = "Posts"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpeg', upload_to='profileImage')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

