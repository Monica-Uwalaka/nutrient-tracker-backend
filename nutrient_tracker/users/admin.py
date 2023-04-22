from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Goal

# Register your models here.
class GoalAdmin(admin.ModelAdmin):
    fields = ["id","user", "calories", "protein", "carbohydrate", "fats", "start_date", "end_date"]
    list_display = ("id", "user", "calories", "protein", "carbohydrate", "fats", "start_date", "end_date")

admin.site.register(User, UserAdmin)
admin.site.register(Goal, GoalAdmin)
