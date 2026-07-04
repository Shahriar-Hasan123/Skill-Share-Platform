from django.contrib import admin
from .models import Profile, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "location", "created_at"]
    search_fields = ["user__username", "location"]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display=["name","category","user","created_at"]
    list_filter=["category"]
    search_fields=["name","user__user_name"]