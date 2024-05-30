from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True) 
    posts = models.ManyToManyField('Post', through='UserPost')


    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(unique=True)
    date_scraped = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)