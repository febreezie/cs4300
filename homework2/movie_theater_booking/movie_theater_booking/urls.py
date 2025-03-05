from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('bookings.urls')),  
]
