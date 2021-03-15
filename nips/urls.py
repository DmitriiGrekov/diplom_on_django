from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r"^$", include("mainpage.urls")),
    url(r"^players", include("players.urls")),
    url(r"^history", include("history.urls")),
    url(r"^achivments", include("achivments.urls")),
    url(r"^account", include("register.urls")),
    url(r"^login", include("loginapp.urls")),
    url(r"^logout", include("logoutapp.urls")),
    url(r'^success', include('successapp.urls')),
    ]
