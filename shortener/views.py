from django.shortcuts import redirect, get_object_or_404
from .models import ShortLink


def redirect_short_link(request, path):
    """Redirect from short path to target URL."""
    short_link = get_object_or_404(ShortLink, path=path)
    return redirect(short_link.target_url)
