# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Results(models.Model):
    index = models.IntegerField(blank=True, primary_key=True)
    date = models.TextField(blank=True, null=True)
    day = models.TextField(blank=True, null=True)
    solved_date = models.TextField(blank=True, null=True)
    elapsed_seconds = models.IntegerField(blank=True, null=True)
    solved = models.IntegerField(blank=True, null=True)
    checked = models.IntegerField(blank=True, null=True)
    revealed = models.IntegerField(blank=True, null=True)
    streak_eligible = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'results'