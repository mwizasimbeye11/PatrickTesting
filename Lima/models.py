from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.contrib.auth.models import User




from django.db import models
from django.core.mail import send_mail
import random, string
# Create your models here.
def random_string():
    return str(random.randint(10000, 99999))

def agent_id():
    return 'MA'+str(random.randint(100, 999))

class Person(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    person_id = models.CharField(max_length=5, default=agent_id, editable=False)
    password = models.CharField(max_length=5, default=random_string, editable=True)

class Markets(models.Model):
    pass

class Agent(Person,models.Model):
    MARKETS = (('Lusaka', 'Soweto'), ('Kabwe', 'New Kasanda'), ('Ndola', 'Masala'), ('Kitwe', 'Chisokone'),)
    marketName = models.CharField(max_length=50, choices=MARKETS)

    def save_auth_1(self):
        return str(self.save)

    def save_auth_2(self):
        return str(self.good)

def send_user_email(sender, instance, **kwargs):
   if kwargs['created']:
       id = instance.agent.person_id
       password = instance.agent.password
       send_mail(
           'Lima Links Accounts',
           'Hello, Admin\n'
           'A new Lima Links market account has created\n'
           'User ID:'+ id +'\n'
           'Password: '+ password +'',
           'mwizasimbeye@gmail.com',
           ['mwiza@bongohive.co.zm'],
           fail_silently=False,
       )

post_save.connect(send_user_email, weak=True, sender=Agent)

class Farmer(Person):
    agentId = models.ForeignKey(Agent,default=1)
    pass


class Crop(models.Model):
    cropName = models.CharField(max_length=40)
