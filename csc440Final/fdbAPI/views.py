from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Competitions, Teams, Matches,Standings
from .serializers import CS, TS, MS,SS


# Create your views here.
@api_view(['GET'])
def getCompetitions(request):
    app = Competitions.objects.all()
    serializer = CS(app, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTeams(request, competition_code=None):
    if competition_code:
        teams = Teams.objects.filter(competitionCode__code=competition_code)
        if not teams.exists():
            return Response(
                {"detail": f"No teams found for competition code: {competition_code}"}
            )
    else:
        teams = Teams.objects.all()

    serializer = TS(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getMatches(request, competition_code=None):
    if competition_code:
        matches = Matches.objects.filter(competitionCode__code=competition_code)
        if not matches.exists():
            return Response(
                {"detail": f"No matches found for competition code: {competition_code}"}
            )
    else:
        matches = Matches.objects.all()

    serializer = MS(matches, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStandings(request, competition_code=None):
    if competition_code:
        standings = Standings.objects.filter(competitionCode__code=competition_code)
        if not standings.exists():
            return Response(
                {"detail": f"No matches found for competition code: {competition_code}"}
            )
    else:
        standings = Standings.objects.all()

    serializer = SS(standings, many=True)
    return Response(serializer.data)