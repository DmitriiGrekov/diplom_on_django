from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Players
from django.urls import reverse


def index(request):
    all_players = Players.objects.order_by('name')
    return render(request, 'player/player.html', {"all_players": all_players})


def detail(request, player_id):
    try:
        p = Players.objects.get(id=player_id)
    except:
        raise Http404("Статья не найдена")
    comment_list = p.comment_set.order_by('-id')
    return render(request, 'player/individual.html',
                  {"p": p, 'comment_list': comment_list})


def leave_comment(request, player_id):
    try:
        p = Players.objects.get(id=player_id)
    except:
        raise Http404("Статья не найдена")
    p.comment_set.create(comment_name=request.POST['name'],
                         comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('players:detail', args=(p.id,)))
