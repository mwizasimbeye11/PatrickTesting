from django.contrib import admin


# Register your models here.
from django.contrib.admin import helpers
from django.template.response import TemplateResponse

from .models import Agent, Market, Crop, Town, Farmer, District , CropToFarmer, Packaging, FarmerToAgent, CropPackaging
from django.db import models
from django.db.models.query import QuerySet


class CropDesign(admin.ModelAdmin):
    list_display = ["name"]


class CropToFarmerDesign(admin.ModelAdmin):
    list_display = ["crop", "farmer"]


class FarmerDesign(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "address", "agent"]


class MarketDesign(admin.ModelAdmin):
    list_display = ["name"]


class TownDesign(admin.ModelAdmin):
    list_display = ["name"]


class DistrictDesign(admin.ModelAdmin):
    list_display = ["name"]


class AgentDesign(admin.ModelAdmin):

    list_display = ["id", "first_name", "last_name", "phone_number", "address"]


class PackagingDesign(admin.ModelAdmin):
    list_display = ["name"]


class CropPackagingDesign(admin.ModelAdmin):
    list_display = ["crop", "market", "packaging"]


class FarmerToAgentDesign(admin.ModelAdmin):
    list_display = ["farmer", "agent"]


admin.site.register(Farmer, FarmerDesign)
admin.site.register(CropToFarmer, CropToFarmerDesign)
admin.site.register(Agent, AgentDesign)
admin.site.register(Crop, CropDesign)
admin.site.register(District, DistrictDesign)
admin.site.register(Market, MarketDesign)
admin.site.register(Town, TownDesign)
admin.site.register(Packaging, PackagingDesign)
admin.site.register(FarmerToAgent, FarmerToAgentDesign)
admin.site.register(CropPackaging, CropPackagingDesign)
