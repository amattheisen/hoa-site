import datetime
from django.db import models
from django.utils import timezone
from django import forms


class Category(models.Model):
    category_title = models.CharField(max_length=20)
    category_description = models.CharField(max_length=250)
    def __str__(self):
        return self.category_title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_text = models.TextField(max_length=2500)
    pub_date = models.DateTimeField('Date published')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=31) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
