from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>", views.MenuItemView.as_view()),
    path('book/', views.BookingView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("api-token-auth/", obtain_auth_token),
]