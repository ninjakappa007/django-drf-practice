from django.contrib import admin
from .models import JobModel, ProposalModel

admin.site.register(JobModel)
admin.site.register(ProposalModel)