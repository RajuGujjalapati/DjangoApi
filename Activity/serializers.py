from rest_framework import serializers
from .models import User, ActivityPeriod
from random import randrange
class Apiserializer(serializers.ModelSerializer):
    # choices  = ApiActivity(many=True)
    class Meta:
        model =User
        fields  = ['id','user_name','time_zone','choices']  
class ApiActivity(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityPeriod
        for _ in range(randrange(1,4)):
            fields = ('user_id',"start_time", 'end_time',)
        #read_only_fields = ('start_time',)
        depth=2
       