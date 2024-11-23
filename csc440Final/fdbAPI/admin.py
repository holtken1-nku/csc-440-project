from django.contrib import admin
from .models import Competitions,Teams,Matches,Standings


admin.site.register(Competitions)
admin.site.register(Teams)
admin.site.register(Matches)
admin.site.register(Standings)