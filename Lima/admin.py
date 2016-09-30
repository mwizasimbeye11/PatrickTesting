from django.contrib import admin

# Register your models here.
from .models import Person
from .models import Farmer
from .models import Agent
from .models import Markets
from .models import Crop


class cropDesign(admin.ModelAdmin):
    list_display = ["cropName"]


class farmerDesign(admin.ModelAdmin):    list_display = ["firstName", "lastName", "address", "district","agentId"]


class MarketDesign(admin.ModelAdmin):
    list_display = ["marketName","townName"]

class agentDesign(admin.ModelAdmin):

    list_display = ["person_id", "firstName","lastName","address","district","marketName"]

#admin.site.register(Farmer,farmerDesign)
#admin.site.register(Markets,MarketDesign)
admin.site.register(Agent,agentDesign)
admin.site.register(Crop,cropDesign)
