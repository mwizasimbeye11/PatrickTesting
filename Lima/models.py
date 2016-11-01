from __future__ import unicode_literals

from django.db import transaction
from django.db import models
import random

# Create your models here.


def random_string():
    return str(random.randint(10000, 99999))


def agent_id():
    return str(random.randint(100, 999))


def choice(market):

        return market


class Person(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone_number = models.IntegerField(max_length=10)
    password = models.CharField(max_length=5, default=random_string, editable=True)


class District(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Town(models.Model):

    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    # transaction.commit()  # Whenever you want to see

    def __unicode__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=50)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


def get_queryset(self):
    mylist = []
    transaction.commit()  # Whenever you want to see
    data = Market.objects.all()

    for e in data:
        mylist.append((e.name, e.name), )
        m = tuple(mylist)
    return m


class Agent(Person, models.Model):
    market = models.ForeignKey(Market, default=1)

"""
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
           'Name: ' + name + '\n'
           'User ID:' + id + '\n'
           'Password: ' + password + '',
           'mwizasimbeye@gmail.com',
           ['patrick@bongohive.co.zm'],
           fail_silently=False,
        )

post_save.connect(send_user_email, weak=True, sender=Agent)

"""


class Farmer(Person):
    town = models.ForeignKey(Town, default=1)
    market_agent = models.CharField(Agent, max_length=10)


class Crop(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class CropToFarmer(models.Model):
    crop = models.CharField(max_length=40)
    farmer = models.CharField(max_length=40)


class Packaging(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class CropPackaging(models.Model):
    crop = models.ForeignKey(Crop, max_length=40)
    market = models.ForeignKey(Market, max_length=40)
    packaging = models.ForeignKey(Packaging, max_length=40)


class FarmerToAgent(models.Model):
    farmer = models.ForeignKey(Farmer, max_length=40)
    agent = models.ForeignKey(Agent, max_length=40)

