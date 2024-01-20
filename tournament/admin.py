from django.contrib import admin
from tournament.models import Tournament
# Register your models here.


@admin.register(Tournament)
class user_display(admin.ModelAdmin):
  list_display = Tournament.data_display
