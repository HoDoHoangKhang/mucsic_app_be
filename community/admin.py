from django.contrib import admin

# Register your models here.
from .models import Fandom, FandomMember, PrivateMessage, GroupMessage

admin.site.register(Fandom)
admin.site.register(FandomMember)
admin.site.register(PrivateMessage)
admin.site.register(GroupMessage)