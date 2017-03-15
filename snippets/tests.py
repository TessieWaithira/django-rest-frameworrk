from django.test import TestCase
from .models import Snippets
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    def setUp(self):
        self.snippets_name = "Write code"
        self.snippets = Snippets(name=self.snippets_name)

    def test_model_can_create_a_snippet(self):
        old_count = Snippets.objects.count()
        self.snippets.save()
        new_count = Snippets.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.snippets_data = {'name': 'Write code'}
        self.response = self.cliemt.post(
            reverse('create'),
            self.snippets_data,
            format="json")

    """create"""
    def test_api_can_create_a_snippet(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    """read"""
    def test_api_can_get_a_snippet(self):
        snippet = Snippets.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': snippet.id}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_OK)
        self.assertContains(response, snippet)

    """Update"""
    def test_api_can_update_a_snippet(self):
        change_snippet = {'name': 'This is an update'}
        res = self.client.put(
            reverse('details', kwargs={'pk': snippet.id}),
            change_snippet, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_201_OK)

    """Delete"""
    def test_Api_can_delete_a_snippet(self):
        snippet = Snippets.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk':snippet.id}),
            format="json", follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_NO_CONTENT)

