from django.contrib import admin


# Register your models here.
from django.contrib.admin import helpers
from django.template.response import TemplateResponse

from .models import Agent
from .models import Market
from .models import Crop
from .models import Town
from .models import District
from .models import Farmer
from django.db import models
from django.db.models.query import QuerySet


def Verify(modeladmin,request,QuerySet):
        QuerySet.update(verified=True)
        QuerySet.update


def Unverify(modeladmin,request,QuerySet):
        QuerySet.update(verified=False)

class cropDesign(admin.ModelAdmin):
    list_display = ["crop_name",'verified']
    actions = [Verify,Unverify]


class farmerDesign(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "address","agentId"]


class MarketDesign(admin.ModelAdmin):
    list_display = ["market_name"]


class TownDesign(admin.ModelAdmin):
    list_display = ["town_name"]

class DistrictDesign(admin.ModelAdmin):
    list_display = ["district_name"]

class agentDesign(admin.ModelAdmin):

    list_display = ["person_id", "first_name","last_name", "phone_number", "address",]

admin.site.register(Farmer,farmerDesign)
#admin.site.register(Markets,MarketDesign)
admin.site.register(Agent,agentDesign)
#admin.site.register(Crop,cropDesign)
admin.site.register(Crop,cropDesign)
admin.site.register(District, DistrictDesign)
admin.site.register(Market, MarketDesign)
admin.site.register(Town, TownDesign)