import random
import string
from django.db import models


def generate_short_path():
    """Generate a random 6-8 character string for the short URL path."""
    length = random.randint(6, 8)
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


class ShortLink(models.Model):
    path = models.CharField(
        max_length=8,
        unique=True,
        default=generate_short_path,
        help_text="Unique short path for the URL",
    )
    target_url = models.URLField(
        max_length=2048, help_text="The target URL to redirect to"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Short Link"
        verbose_name_plural = "Short Links"

    def __str__(self):
        return f"{self.path} -> {self.target_url}"

    def get_short_url(self):
        """Returns the full short URL (for display purposes)."""
        return f"/{self.path}"
