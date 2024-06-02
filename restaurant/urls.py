from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.MenuItemView.as_view()),
    path('books/', views.BookingView.as_view()),
    path('books/<int:pk>', views.BookingViewDetails.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
    path("api-token-auth/", obtain_auth_token),
]