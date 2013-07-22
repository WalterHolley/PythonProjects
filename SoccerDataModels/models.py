from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=255)

class League(models.Model):
    country_id = models.ForeignKey(Country)
    league_name = models.CharField(max_length=255)
    source_identifier = models.CharField(max_length=255)

class Division(models.Model):
    league_id = models.ForeignKey(League)
    division_name = models.CharField(max_length=255)
    source_identifier = models.CharField(max_length=255, default='none')

class Stadium(models.Model):
    country_id = models.ForeignKey(Country)
    stadium_name = models.CharField(max_length=255)  

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    country_id = models.ForeignKey(Country)
    stadium_id = models.ForeignKey(Stadium)
    source_identifier = models.CharField(max_length=255)
    wiki_page = models.CharField(max_length=255)
    team_website = models.CharField(max_length=255)
    
class Season(models.Model):
    league_id = models.ForeignKey(League)
    season_name = models.CharField(max_length=255)
    season_start = models.DateField()
    season_end = models.DateField()
    
class TeamDivision(models.Model):
    division_id = models.ForeignKey(Division)
    team_id = models.ForeignKey(Team)
    season_id = models.ForeignKey(Season)
