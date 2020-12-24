from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'All Teams Statistic', views.AllTeamsStatistic, basename="AllTeams")
router.register(r'Top 3 Teams', views.Top3Teams, basename="Top3")
router.register(r'Final Winner', views.FinalWinner, basename="Final Winner")

urlpatterns = [
    path('api/', include(router.urls)),
    path('aou-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.start),
    path('input_teams/', views.input_teams),
    path('api/<str:team_name>', views.TeamView.as_view())
]
