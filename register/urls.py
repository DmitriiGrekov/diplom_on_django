from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.register, name='signup'),
    url(r'^/confirmed$', views.confirmed, name='confirmed'),
    url(r'^/edit', views.edit, name='edit'),
    url(r'^/profile', views.profile, name='profile'),
]
