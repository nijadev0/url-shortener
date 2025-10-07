"""
Simple tests for the URL shortener
Run with: python manage.py test
"""

from django.test import TestCase, Client
from django.urls import reverse
from shortener.models import ShortLink


class ShortLinkModelTest(TestCase):
    def test_shortlink_creation(self):
        """Test that a ShortLink can be created with auto-generated path"""
        link = ShortLink.objects.create(target_url="https://example.com")
        self.assertIsNotNone(link.path)
        self.assertTrue(6 <= len(link.path) <= 8)
        self.assertEqual(link.target_url, "https://example.com")

    def test_custom_path(self):
        """Test that a custom path can be used"""
        link = ShortLink.objects.create(path="custom", target_url="https://example.com")
        self.assertEqual(link.path, "custom")

    def test_unique_path(self):
        """Test that paths are unique"""
        ShortLink.objects.create(path="test123", target_url="https://example.com")
        # Creating another with the same path should raise an error
        with self.assertRaises(Exception):
            ShortLink.objects.create(path="test123", target_url="https://another.com")


class RedirectViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.link = ShortLink.objects.create(
            path="testpath", target_url="https://example.com"
        )

    def test_redirect(self):
        """Test that accessing a short link redirects to target URL"""
        response = self.client.get(f"/{self.link.path}")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, self.link.target_url)

    def test_404_for_nonexistent_path(self):
        """Test that a non-existent path returns 404"""
        response = self.client.get("/nonexistent")
        self.assertEqual(response.status_code, 404)

    def test_root_redirects_to_admin(self):
        """Test that root URL redirects to admin"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertTrue("/admin/" in response.url)
