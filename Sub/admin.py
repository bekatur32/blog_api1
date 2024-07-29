from django.contrib import admin
from .models import Subscribed

@admin.register(Subscribed)
class subriedsAdmin(admin.ModelAdmin):
    model = Subscribed
    list_display = ['email','password']
