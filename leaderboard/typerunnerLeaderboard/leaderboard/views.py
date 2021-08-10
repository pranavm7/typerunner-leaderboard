from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScoreboardSerializer
from .models import Scoreboard


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/score-list/',
        'Detail View' : '/score-detail/<str:pk>/',
        'Create' : '/score-create/',
        'Update' : '/score-update/<str:pk>/',
        'Delete' : '/score-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def scores(request):
    top5Scores = Scoreboard.objects.all().order_by('-score')[:5]
    serializer = ScoreboardSerializer(top5Scores, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def scoreCreate(request):
    serializer = ScoreboardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)