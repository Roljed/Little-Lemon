from django.urls import include, path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("menu/", views.MenuItemsView.as_view(), name="menu"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-item"),
    path("bookings/", include(router.urls), name="bookings"),
    path("book", views.book, name="book"),
    path("reservations/", views.ReservationsView.as_view(), name="reservations"),
    path("api-token-auth/", obtain_auth_token),
]
