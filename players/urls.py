from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'players'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('/<int:player_id>/', views.detail, name='detail'),
    path('/<int:player_id>/leave_comment',
         views.leave_comment, name='leave_comment')
]
