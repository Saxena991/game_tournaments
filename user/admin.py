from django.contrib import admin
from user.models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class user_display(admin.ModelAdmin):
  list_display = UserProfile.data_display
  

