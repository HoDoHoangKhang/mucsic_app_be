from django.contrib import admin

# Register your models here.
from .models import User, Artist, Follower

admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Follower)