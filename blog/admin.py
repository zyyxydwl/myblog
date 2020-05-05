from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from . import models
from .models import Artical


class ArticalAdmin(admin.ModelAdmin):
    list_display = ("title","content","pub_date")
    list_filter = ("pub_date",)
admin.site.register(Artical,ArticalAdmin)
