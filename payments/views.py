from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from .models import Subscription, Transaction
from .serializers import SubscriptionSerializer, TransactionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_premium(request):
    package_type = request.data.get('package_type')
    payment_method = request.data.get('payment_method')
    
    if not package_type or not payment_method:
        return Response(
            {"error": "Thiếu thông tin package_type hoặc payment_method"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Kiểm tra xem user đã có subscription đang hoạt động chưa
    active_subscription = Subscription.objects.filter(
        user=request.user,
        status='active',
        expired_at__gt=timezone.now()
    ).first()
    
    if active_subscription:
        return Response(
            {"error": "Bạn đã có gói premium đang hoạt động"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Xác định thời gian và giá tiền dựa trên loại gói
    if package_type == 'FREE':
        duration_days = 7
        amount = 0
    elif package_type == 'MONTHLY':
        duration_days = 30
        amount = 299000
    elif package_type == 'YEARLY':
        duration_days = 365
        amount = 999000
    else:
        return Response(
            {"error": "Loại gói không hợp lệ"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Tạo subscription mới
    expired_at = timezone.now() + timedelta(days=duration_days)
    subscription = Subscription.objects.create(
        user=request.user,
        status='active',
        expired_at=expired_at
    )
    
    # Tạo transaction nếu không phải gói miễn phí
    if amount > 0:
        Transaction.objects.create(
            user=request.user,
            amount=amount,
            transaction_type='subscription',
            payment_method=payment_method
        )
    
    return Response(
        {
            "message": "Mua gói premium thành công",
            "subscription": SubscriptionSerializer(subscription).data
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_premium_status(request):
    subscription = Subscription.objects.filter(
        user=request.user,
        status='active'
    ).first()
    
    if not subscription:
        return Response(
            {"status": "inactive"},
            status=status.HTTP_200_OK
        )
    
    return Response(
        {
            "status": "active",
            "subscription": SubscriptionSerializer(subscription).data
        },
        status=status.HTTP_200_OK
    )
