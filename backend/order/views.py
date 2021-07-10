from .models import Order
from rest_framework import generics
from .serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderView(generics.ListCreateAPIView):
    ''' API endpoint for order list, just owner can access it '''
    def get_queryset(self):
        user  = self.request.user
        return Order.objects.filter(client=user)
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
