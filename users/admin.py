from django.contrib import admin
from .models import Author, Subscribed

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author

@admin.register(Subscribed)
class subriedsAdmin(admin.ModelAdmin):
    model = Subscribed

