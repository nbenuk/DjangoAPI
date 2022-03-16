from ast import Mod
from atexit import register
from django.contrib import admin
from .models import Rating, Module, Professor, ModuleInstance
# Register your models here.
admin.site.register(Rating)
admin.site.register(Module)
admin.site.register(ModuleInstance)
admin.site.register(Professor)
