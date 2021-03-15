from django.conf.urls import url
from django.views.generic import ListView
from history.models import History

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=History.objects.all(),
                                template_name="history/history.html"))
]
