from django.urls import path
from . import views

urlpatterns = [
    path("<str:path>", views.redirect_short_link, name="redirect"),
]
