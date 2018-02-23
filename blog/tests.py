import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 31 days.
        """
        time = timezone.now() - datetime.timedelta(days=31, seconds=1)
        old_post = Post(pub_date=time)
        self.assertIs(old_post.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last 31 days.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Post(pub_date=time)
        self.assertIs(recent_post.was_published_recently(), True)
