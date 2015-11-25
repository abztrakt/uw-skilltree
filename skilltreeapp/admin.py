from django.contrib import admin

from .models import *

@admin.register(LearningConcept)
class LearningConcept(admin.ModelAdmin):
    pass

@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Prerequisite)
class Prerequisite(admin.ModelAdmin):
    pass
