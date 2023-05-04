from django.contrib import admin
from .models import Massages, Cosmetolog, Specialists, Client, Comment



class DisplayAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')

class imageAdmin(admin.ModelAdmin):
    list_display = ["name", "photo", "position", "additional"]

class ContactAdmin(admin.ModelAdmin):
    pass

  
admin.site.register(Massages, DisplayAdmin)
admin.site.register(Cosmetolog, DisplayAdmin)
admin.site.register(Specialists, imageAdmin)
admin.site.register(Client, ContactAdmin)
admin.site.register(Comment)
