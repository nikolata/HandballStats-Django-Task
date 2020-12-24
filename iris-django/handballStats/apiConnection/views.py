from django.shortcuts import render, redirect
from rest_framework import viewsets
from .multithreading import ProducerThread, ConsumerThread, q
from .serializers import TeamSerializer
from .models import Team
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics


class AllTeamsStatistic(viewsets.ModelViewSet):
    queryset = Team.objects.order_by('-wins', 'name')
    serializer_class = TeamSerializer


class Top3Teams(viewsets.ModelViewSet):
    queryset = Team.objects.order_by('-wins')[:3]
    serializer_class = TeamSerializer


class FinalWinner(viewsets.ModelViewSet):
    queryset = Team.objects.order_by('-last_win')[:1]
    serializer_class = TeamSerializer


class TeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, team_name, *args, **kwargs):
        try:
            team_from_url = Team.objects.get(name=team_name)
        except Team.DoesNotExist:
            return HttpResponse('<p> There is no team with this name in DB</p>')
        serializer = TeamSerializer(team_from_url)
        return Response(serializer.data)


def start(request):
    if request.method == "POST":
        q.queue.clear()
        Team.objects.all().delete()
        c = ConsumerThread(name='consumer')
        print("Consumer Thread is starting")
        c.start()
        request.session['id'] = Team.objects.values('id').order_by('-id').first()
        return redirect('input_teams/')

    return render(request, 'start.html')


def input_teams(request):
    p = ProducerThread(name='producer')
    if request.method == "POST":
        if request.POST['game'] == "stop":
            return redirect('/api/')
        p.run(request.POST['game'])
    return render(request, 'input.html')
