from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated


class MenuItemsView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    model = Menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    model = Menu
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingView(ModelViewSet):
    model = Booking
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

