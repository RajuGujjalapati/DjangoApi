from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Apiserializer, ApiActivity
from .models import User, ActivityPeriod
# Create your views here.

class ApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Apiserializer
class ApiView1(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ApiActivity
    # def create(self,request,*args,**kwargs):
    #     user_data = request.data
    #     usr_try  = User.objects.create(user_plan  = User.objects.get(id=user_data["user_name"]), time_zone = user_data["time_zone"])
    #     usr_try.save()
    #     serializer = Ausr_try  = User(usr_try)
    #     return Response(serializer.data)
