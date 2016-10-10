from django.contrib import admin


# Register your models here.
from .models import Person
from .models import Farmer
from .models import Agent
from .models import Market
from .models import Crop
from .models import Town



class cropDesign(admin.ModelAdmin):
    list_display = ["crop_name"]


class farmerDesign(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "address", "district","agentId"]


class MarketDesign(admin.ModelAdmin):
    list_display = ["market_name"]


class TownDesign(admin.ModelAdmin):
    list_display = ["town_name"]

class agentDesign(admin.ModelAdmin):

    list_display = ["person_id", "first_name","last_name", "phone_number", "address","district",]

#admin.site.register(Farmer,farmerDesign)
#admin.site.register(Markets,MarketDesign)
admin.site.register(Agent,agentDesign)
admin.site.register(Crop,cropDesign)
# admin.site.register(Town, TownClassAdmin)
admin.site.register(Market, MarketDesign)
admin.site.register(Town, TownDesign)