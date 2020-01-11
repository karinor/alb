from django.shortcuts import render
from collections import deque
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import FormView
from .stuff import SearchApi, KillboardApiParser


class RecentSearches:
    def __init__(self):
        self.__history = deque()
        self._count = 0

    @property
    def history(self):
        for e in self.__history:
            yield e

    @history.setter
    def history(self, request):
        if self._count == 10:
            if request not in self.__history:
                self.__history.pop()
                self.__history.appendleft(request)
        else:
            if request not in self.__history:
                self.__history.appendleft(request)
                self._count += 1


rec_history = RecentSearches()


# Create your views here.
class AlbionApiSearchView(TemplateView):
    template_name = 'base.html'

    #  Прилепить историю поиска
    def get(self, request, *args, **kwargs):
        req = request.GET.get("req")
        if req is not None:
            rec_history.history = req
            context = {'req_obj': SearchApi.Search(req), 'recent_searches': rec_history.history}
            return render(request, 'base.html', context)
        else:
            return render(request, 'base.html')


class PlayerView(TemplateView):
    template_name = 'player.html'

    def get(self, request, *args, **kwargs):
        if len(kwargs) == 1:
            context = {'player': KillboardApiParser.Player(kwargs['id'])}
            return render(request, 'player.html', context)


class GuildView(TemplateView):
    template_name = 'player.html'

    def get(self, request, *args, **kwargs):
        if len(kwargs) == 1:
            context = {'player': KillboardApiParser.Player(kwargs['id'])}
            return render(request, 'player.html', context)