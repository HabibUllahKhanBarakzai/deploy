from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import HerokuModel
from  .serializers import HerokuSerializers
# Create your views here.

class HerokuViewsets(ModelViewSet):
    model = HerokuModel
    serializer_class = HerokuSerializers
    queryset = HerokuModel.objects.all()