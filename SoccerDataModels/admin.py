'''
Created on Jul 15, 2013

@author: zero
'''
from django.contrib import admin
from SoccerDataModels.models import Country, Division, League, Season, Stadium, Team

admin.site.register(Country)
admin.site.register(Division)
admin.site.register(League)
admin.site.register(Season)
admin.site.register(Stadium)
admin.site.register(Team)
