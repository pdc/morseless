"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client


class OldStyleTestCase(TestCase):
    def test_nothing(self):
        self.response = self.client.get('/', {})

        self.then_should_succeed()
        self.assertTrue('text' not in self.response.context)

    def test_splits_latters_at_spaces(self):
        self.response = self.client.get('/', {'morse': '.... . .-.. .-.. ---'})

        self.then_should_display_text('HELLO')

    def test_allows_slash_as_word_space(self):
        self.response = self.client.get('/', {'morse': '- .... .-. --- ..- --. .... / .... . .-. .'})

        self.then_should_display_text('THROUGH HERE')

    def then_should_succeed(self):
        self.assertEqual(200, self.response.status_code)

    def then_should_display_text(self, expected):
        self.assertEqual(200, self.response.status_code)
        self.assertEqual(expected, self.response.context['text'])


class ApiTestCase(TestCase):
    def test_nothing(self):
        self.when_client_requests_decode_morse('.... . .-.. .-.. ---')

        self.then_should_return_text('HELLO')


    def when_client_requests_decode_morse(morse):
        self.response = self.client.get('/decode', {'morse': morse})

    def then_should_return_text(self, expected):
        self.assertEqual(200, self.response.status_code)
        self.object = json.loads(self.response.content)
        self.assertEqual(expected, self.object['text'])