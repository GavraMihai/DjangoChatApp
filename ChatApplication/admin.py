from django.contrib import admin
from ChatApplication.models import Account, Room, Message

# Register your models here.
admin.site.register(Account)
admin.site.register(Room)
admin.site.register(Message)
