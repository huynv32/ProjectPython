from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=355)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class News(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=355)
    audio = models.FileField(upload_to='audio/')
    video = models.FileField(upload_to="video/")
    image = models.FileField(upload_to='image/')
    # dateCreated = models.DateTimeField(null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.content


class Image_News(models.Model):
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.FileField(upload_to='image/')
