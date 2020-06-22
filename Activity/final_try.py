import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Activity.settings')
import django
django.setup()
from faker import faker
import fake_gen
fakegen = Faker()
names =[fake_gen.FakeDataFactory('firstName') for _ in range(10)]
def add_user(user_name = names):
    data = User.objects.get_or_create(user_name = names)
    data.save()
    return data
