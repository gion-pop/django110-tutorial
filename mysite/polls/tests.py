import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        `was_published_recently()` should return `False` for questions
        whose `pub_date` is in the future.
        """
        future = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        `was_published_recently()` should return `False` for questions
        whose `pub_date` is older than 1 day.
        """
        past = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(pub_date=past)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        `was_published_recently()` should return `True` for questions
        whose `pub_date` is within the last day.
        """
        recent = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=recent)
        self.assertIs(recent_question.was_published_recently(), True)
