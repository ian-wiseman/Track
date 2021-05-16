from django.db import models

# Create your models here.
class Recruiter(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    commission = models.FloatField()

class Placement(models.Model):

    placement_revenue = models.FloatField()
    client_find = models.CharField(max_length=30)
    client_find_revenue = models.FloatField()
    client_owner = models.CharField(max_length=30)
    client_owner_revenue = models.FloatField()
    candidate_find = models.CharField(max_length=30)
    candidate_find_revenue = models.FloatField()
    candidate_owner = models.CharField(max_length=30)
    candidate_owner_revenue = models.FloatField()