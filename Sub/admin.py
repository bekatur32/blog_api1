from django.contrib import admin
from .models import Subscribed,Subscription

@admin.register(Subscribed)
class subriedsAdmin(admin.ModelAdmin):
    model = Subscribed
    list_display = ['email','password']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'author', 'subscribed_at')
    list_filter = ('subscribed_at',)
