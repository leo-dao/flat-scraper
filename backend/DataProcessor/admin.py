from django.contrib import admin
from .models import User, Post, UserPost
from django.utils import timezone
from django_q.models import Schedule
from .utils import scrape_posts_daily
from .tasks import send_weekly_update

admin.site.register(User)
admin.site.register(Post)
admin.site.register(UserPost)

Schedule.objects.create(
    func='myapp.utils.scrape_posts_daily',
    schedule_type=Schedule.DAILY,
    next_run=timezone.now()
)

Schedule.objects.create(
    func='myapp.tasks.send_weekly_update',
    schedule_type=Schedule.WEEKLY,
    next_run=timezone.now()
)