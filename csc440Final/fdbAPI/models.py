from django.db import models


class Competitions(models.Model):
    id = models.IntegerField(primary_key=True)
    areaOfCompetition = models.CharField(max_length=50)
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=10, unique=True)


class Teams(models.Model):
    teamId = models.IntegerField()
    competitionCode = models.ForeignKey(Competitions, on_delete=models.CASCADE, to_field='code', default='')
    name = models.CharField(max_length=25, null=True)
    founded = models.IntegerField(default=0, null=True)
    venue = models.CharField(max_length=25, null=True)
    coachName = models.CharField(max_length=40, default='', null=True)
    squad = models.JSONField(default=dict, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['competitionCode', 'teamId'], name='unique_competition_id')
        ]

    def __str__(self):
        return str(self.competitionCode_id)


class Matches(models.Model):
    matchId = models.IntegerField()
    competitionCode = models.ForeignKey(Competitions, on_delete=models.CASCADE, to_field='code', default='')
    matchDateUTC = models.DateTimeField()
    updateDate = models.DateTimeField()
    homeTeamId = models.IntegerField(null=True)
    homeTeamName = models.CharField(max_length=25, null=True)
    awayTeamId = models.IntegerField(null=True)
    awayTeamName = models.CharField(max_length=25, null=True)
    winner = models.CharField(max_length=25, null=True)
    halfTimeHomeGoals = models.IntegerField(null=True)
    halfTimeAwayGoals = models.IntegerField(null=True)
    fullTimeHomeGoals = models.IntegerField(null=True)
    fullTimeAwayGoals = models.IntegerField(null=True)

    def __str__(self):
        return str(self.matchId)


class Standings(models.Model):
    competitionCode = models.ForeignKey(Competitions, on_delete=models.CASCADE, to_field='code', default='')
    seasonStage = models.CharField(max_length=25)
    teamId = models.IntegerField()
    teamName = models.CharField(max_length=25, null=True)
    position = models.IntegerField()
    playedGames = models.IntegerField()
    gamesWon = models.IntegerField()
    gamesDrawn = models.IntegerField()
    gamesLost = models.IntegerField()
    points = models.IntegerField()
    goalsFor = models.IntegerField()
    goalsAgainst = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['competitionCode', 'seasonStage', 'teamId'],
                                    name='unique_competition_seasonStage_teamId')
        ]

    def __str__(self):
        return str(self.competitionCode_id) + "," + str(self.seasonStage) + "," + str(self.teamId)
