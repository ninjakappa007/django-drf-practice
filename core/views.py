from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import JobModel, ProposalModel
from .serializer import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = JobModel.objects.all()
    serializer_class = JobSerializer
