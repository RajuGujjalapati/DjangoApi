from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Phone
# Create your views here.
def my_view(request):
    user = User.objects.get(id=1)
    print(user.phone)