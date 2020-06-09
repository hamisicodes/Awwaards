from django.contrib import admin
from .models import Profile,Project,Rate


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user','bio')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display =('title','description','author','publish_at')

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display =('usability','design','content')




