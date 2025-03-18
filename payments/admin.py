from django.contrib import admin

# Register your models here.
from .models import Subscription, Transaction

admin.site.register(Subscription)
admin.site.register(Transaction)