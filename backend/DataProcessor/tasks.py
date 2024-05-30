from django.core.mail import send_mail
from .models import User, Post
from datetime import timedelta
from django.utils import timezone

def send_weekly_update():
    users = User.objects.all()
    posts = Post.objects.filter(date_scraped__gte=timezone.now() - timedelta(days=7))

    for user in users:
        user_posts = posts.filter(user=user)
        if user_posts:
            from django.core.mail import send_mail
from .models import User, Post

def send_weekly_update():
    users = User.objects.all()
    posts = Post.objects.filter(date_scraped__gte=timezone.now() - timedelta(days=7))

    for user in users:
        subject = 'Your weekly post update'
        message = 'You have new posts this week.'
        from_email = 'fake@email.com'  # Replace with email
        to_email = [user.email]  # Replace with the user's email

        # Send email
        send_mail(subject, message, from_email, to_email)
