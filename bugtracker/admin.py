from django.contrib import admin
from bugtracker.models import Author, Ticket
from django.contrib.auth.admin import UserAdmin


admin.site.register(Author, UserAdmin)
admin.site.register(Ticket)
