from django.db import models
from django.conf import settings

class JobCategoryEnum(models.TextChoices):
    FULL_TIME = 'Full_time', 'full_time'
    PART_TIME = 'Part_time', 'part_time'


# Create your models here.
class JobModel(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, db_index=True)
    description = models.TextField()
    budget = models.IntegerField(blank=False, null=False)
    category = models.CharField(max_length=255, choices= JobCategoryEnum.choices, default=JobCategoryEnum.FULL_TIME)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

class ProposalModel(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE, blank=False, null=False)
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    bid_amount = models.IntegerField(blank=False, null=False)
    message = models.TextField()