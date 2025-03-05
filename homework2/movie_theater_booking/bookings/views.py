from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.utils import timezone
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})



@login_required
def book_now(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    seats = Seat.objects.filter(is_booked=False)

    if request.method == "POST":
        seat = get_object_or_404(Seat, pk=request.POST["seat_id"], is_booked=False)
        seat.is_booked = True
        seat.save()
        Booking.objects.create(movie=movie, seat=seat, user=request.user, booking_date=timezone.now())
        messages.success(request, f"Seat {seat.seat_number} booked successfully!")
        return redirect("past_booking")

    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "seats": seats
    })

@login_required
def booking_history_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': user_bookings})

def auth_view(request):
    """ Unified login/signup page that redirects back to the last page after login. """
    if request.user.is_authenticated:
        return redirect("past_booking")

    # Get the next URL to redirect after login/signup
    next_url = request.GET.get("next", "past_booking")  # Default to past bookings if not provided

    login_form = AuthenticationForm(request, data=request.POST or None)
    signup_form = UserCreationForm(request.POST or None)
    error_message = None

    if request.method == "POST":
        if "login_submit" in request.POST:
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user:
                    login(request, user)
                    return redirect(next_url)  # Redirect to where the user came from
                else:
                    error_message = "Invalid username or password."

        elif "signup_submit" in request.POST:
            if signup_form.is_valid():
                user = signup_form.save()
                user.set_password(signup_form.cleaned_data["password1"])  # Hash password
                user.save()

                authenticated_user = authenticate(
                    request, 
                    username=signup_form.cleaned_data["username"], 
                    password=signup_form.cleaned_data["password1"]
                )

                if authenticated_user:
                    login(request, authenticated_user)
                    return redirect(next_url)  # Redirect back to the booking page
                else:
                    error_message = "Signup successful, but auto-login failed. Try logging in manually."

            else:
                error_message = "Signup error: " + str(signup_form.errors)

    return render(request, "bookings/auth.html", {
        "login_form": login_form,
        "signup_form": signup_form,
        "error_message": error_message,
        "next": next_url  # Pass the next URL to the template
    })