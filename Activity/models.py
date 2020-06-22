from django.db import models
import datetime
from datetime import timedelta
from random import randrange
days = datetime.datetime.now()

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    time_zone = models.CharField(max_length=40)
    #exitimezone = models.TimeField()
    def __str__(self):
        return self.user_name
    @property
    def choices(self):
        return self.activity_period_set.all()
class ActivityPeriod(models.Model):
    # def random_date(start,l):
    #     current = start
    #     while l >= 0:
    #         curr = current + datetime.timedelta(minutes=randrange(60))
    #         yield curr
    #         l-=1
    # startDate = datetime.datetime(2020, randrange(1,12), randrange(1,30),randrange(1,12))    
    # mydata = [res.strftime("%d/%m/%y %H:%M") for res in random_date(startDate,1)]
    # 
    start_time = models.DateTimeField( null=True)
    end_time = models.DateTimeField( null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_time)


#days.strftime("%d")+ " "+random.randint(1,31)+" "+random.randint(1,13)+"  "+days.strftime("%H:%M%p")