from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class MenuItemsView(ListCreateAPIView):
    throttle_classes   = [UserRateThrottle,AnonRateThrottle]
    model = Menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    throttle_classes   = [UserRateThrottle,AnonRateThrottle]
    model = Menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingView(ListCreateAPIView):
    throttle_classes   = [UserRateThrottle,AnonRateThrottle]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class BookingViewDetails(RetrieveUpdateAPIView, DestroyAPIView):
    throttle_classes   = [UserRateThrottle,AnonRateThrottle]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserView(ModelViewSet):
    throttle_classes   = [UserRateThrottle,AnonRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

