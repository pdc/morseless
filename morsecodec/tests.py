"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class OldStyleTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_nothing(self):
        self.response = self.client.get('/', {})

        self.then_should_succeed()
        self.assertTrue('text' not in self.response.context)

    def test_a(self):
        self.response = self.client.get('/', {'morse': '.... . .-.. .-.. ---'})

        self.then_should_display_text('HELLO')

    def then_should_succeed(self):
        self.assertEqual(200, self.response.status_code)

    def then_should_display_text(self, expected):
        self.assertEqual(200, self.response.status_code)
        self.assertEqual(expected, self.response.context['text'])