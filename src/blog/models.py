from django.db import models


# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

# class Blog:
# #     title = "Hello World"
# #     content = "something cool"
