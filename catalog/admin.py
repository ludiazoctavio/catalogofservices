from django.contrib import admin

from .models import Service, Area, Item

admin.site.register(Service)
admin.site.register(Area)
admin.site.register(Item)