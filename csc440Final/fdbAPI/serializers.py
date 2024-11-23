from rest_framework import serializers

from .models import Competitions,Matches,Teams,Standings



class CS(serializers.ModelSerializer):
    class Meta:
        model = Competitions
        fields = '__all__'


class TS(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'


class MS(serializers.ModelSerializer):
    class Meta:
        model = Matches
        fields = '__all__'


class SS(serializers.ModelSerializer):
    class Meta:
        model = Standings
        fields = '__all__'