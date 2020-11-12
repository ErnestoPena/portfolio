from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    parent_id = models.IntegerField(default=0)
    post_title = models.CharField(max_length=80, blank=True)
    meta_title = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=100, blank=True)
    summary = models.CharField(max_length=100, blank=True)
    published = models.BooleanField(blank=False, default=False)
    created = models.DateField(blank=False)
    updated = models.DateField(blank=False)
    published = models.DateTimeField(blank= False)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.post_title

class Comments(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    parent_id = models.IntegerField(blank=False, default=0)
    title = models.CharField(max_length=40, blank=False)
    created = models.DateTimeField(blank=False)
    published = models.DateTimeField(blank=False)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class Categories(models.Model):
    parent_id = models.IntegerField(default=0)
    title = models.CharField(max_length=50, blank=False)
    metatitle = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title


class PostCategory(models.Model):
    post_id = models.ForeignKey(Posts, on_delete= models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
        

class PostMeta(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    postmeta_key = models.CharField(max_length=80, blank=False)
    content = models.TextField(max_length=500)        