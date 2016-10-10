from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.dispatch import dispatcher
from django.db.models import QuerySet
from django.db import transaction



from django.db import models
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
import random, string
# Create your models here.
def random_string():
    return str(random.randint(10000, 99999))

def agent_id():
    return 'MA'+str(random.randint(100, 999))
def Choice(market):

        return market





class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    phone_number = models.IntegerField(max_length=10)
    person_id = models.CharField(max_length=5, default=agent_id, editable=False, primary_key = True)
    password = models.CharField(max_length=5, default=random_string, editable=True)

class Town(models.Model):
    id = models.AutoField(primary_key=True,default=1)
    # town_list = (('Sowet', 'Lusaka'), ('New Kasanda', 'Kabwe'), ('Masala', 'Ndola'), ('Chisokone', 'Kitwe'),)
    town_name = models.CharField(max_length=50)
    # transaction.commit()  # Whenever you want to see

    def __unicode__(self):
        return self.town_name

class Market(models.Model):

    #global market_name
    market_name = models.CharField(max_length=50)
    town_id = models.ForeignKey(Town, default=0)

    def __unicode__(self):
        return self.market_name

def get_queryset(self):
    mylist = []
    #transaction.enter_transaction_management()
    transaction.commit()  # Whenever you want to see
    data = Market.objects.all()

    # data._result_cache = None
    for e in data:
        mylist.append((e.market_name, e.market_name), )
        m = tuple(mylist)
    return m









class Agent(Person,models.Model):

    # MARKETS = (("patrick","sikalinda"),("Mwiza","Simbeye"))
    # market_names = models.CharField(max_length=50, choices=get_queryset(Markets))
    market = models.ForeignKey(Market, default=1)






    #entries = Entry.objects.filter(**kwargs)
    #Markets.save(self)





    #market_name = models.CharField(max_length=50, choices=MARKETS)





def send_user_email(sender, instance, **kwargs):
   if kwargs['created']:
       id = instance.agent.person_id
       password = instance.agent.password
       first_name = instance.agent.first_name
       last_name = instance.agent.last_name
       name = first_name + ' ' + last_name

       send_mail(
           'Limalinks Accounts',
           'Hello, Admin\n'
           'A new Limalinks market agent has been sucessfully added.\n\n'
           'See account information below:\n\n'
           'Name: '+ name +'\n'
           'User ID:'+ id +'\n'
           'Password: '+ password +'',
           'mwizasimbeye@gmail.com',
           ['patrick@bongohive.co.zm'],
           fail_silently=False,
       )

post_save.connect(send_user_email, weak=True, sender=Agent)


class Farmer(Person):
    agentId = models.ForeignKey(Agent,default=1)
    pass

class Crop(models.Model):
    crop_name = models.CharField(max_length=40)