from django.urls import path
from .views import purchase_premium, check_premium_status


urlpatterns = [
    path('premium/purchase/', purchase_premium, name='purchase_premium'),
    path('premium/status/', check_premium_status, name='check_premium_status'),
]