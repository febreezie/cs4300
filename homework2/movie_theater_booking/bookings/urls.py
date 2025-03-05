from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import movie_list_view, book_now, booking_history_view, auth_view

urlpatterns = [
    path('', movie_list_view, name='movie_list'),
    path('book/<int:movie_id>/', book_now, name='book_now'),
    path('past-bookings/', booking_history_view, name='past_booking'),
    path('auth/', auth_view, name='auth'),
    path('logout/', LogoutView.as_view(next_page='movie_list'), name='logout'),
]
