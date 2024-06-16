from django.db import models

PET_CHOICES = [
    (0, 'No pets'),
    (1, 'Dogs allowed'),
    (2, 'Cats allowed'),
]
FURNISHED_CHOICES = [
    (0, 'Unfurnished'),
    (1, 'Furnished'),
    (2, 'Either'),
]

class Preferences(models.Model):
    location = models.CharField(max_length=255)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    availability = models.DateField()
    pets = models.IntegerField(default=0, choices=PET_CHOICES)
    bedrooms = models.IntegerField(null=True)
    furnished = models.IntegerField(default=2, choices=FURNISHED_CHOICES)

class User(models.Model):
    email = models.EmailField(unique=True) 
    preferences = models.OneToOneField(Preferences, on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', through='UserPost')

    def __str__(self):
        return self.email

class Post(models.Model):
    link = models.URLField(unique=True)
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    pets = models.CharField(max_length=255, null=True)
    furnished = models.BooleanField(default=False)
    bedrooms = models.IntegerField(null=True)
    date_scraped = models.DateTimeField(auto_now_add=True)
    date_sent = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.link

class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.email} - {self.post.link}'