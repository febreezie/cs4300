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


#3.3 Implementing the MVT Architecture

#Manages movies using API (Supports CRUD-list,retriece, create,update)
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

#API for seat availability/booking
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

#API for user bookings
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        """Pass request context to serializer."""
        return {'request': self.request}  


#Displays all available movies with "Book Now" button.
def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


#Handles seat booking for specific movie, must be logged in, only shows unbooked seats.
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



#Displays booking history of the logged-in user
@login_required
def booking_history_view(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': user_bookings})




# A unified login and signup page to use for both booking and past bookings viewpage
def auth_view(request):

    #If the user is already authenticated, send them to their past bookings immediately
    if request.user.is_authenticated:
        return redirect("past_booking")

    # Get the next URL to redirect after login/signup
    next_url = request.GET.get("next", "past_booking") 

    #Create authentication forms
    login_form = AuthenticationForm(request, data=request.POST or None)
    signup_form = UserCreationForm(request.POST or None)
    error_message = None

    #If the user submits POST request, determine if it's login or signup
    if request.method == "POST":

        #User Clicks login
        if "login_submit" in request.POST:

            #Check if login valid
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']

                #Authenticate user 
                user = authenticate(request, username=username, password=password)

                if user:
                    login(request, user)
                    return redirect(next_url)  
                else:
                    error_message = "Invalid username or password."
        #User clicked the signup button
        elif "signup_submit" in request.POST:

            #Validate the signup form
            if signup_form.is_valid():

                #Save the new user to the database
                user = signup_form.save()

                #Hard code hashed password
                user.set_password(signup_form.cleaned_data["password1"])  
                user.save()

                #Authenticating new user
                authenticated_user = authenticate(
                    request, 
                    username=signup_form.cleaned_data["username"], 
                    password=signup_form.cleaned_data["password1"]
                )

                #Login new user and put them back to where they were before
                if authenticated_user:
                    login(request, authenticated_user)
                    # Redirect back to the booking page
                    return redirect(next_url) 
                else:
                    error_message = "Signup successful, but auto-login failed. Try logging in manually."

            else:
                error_message = "Signup error: " + str(signup_form.errors)

    #Render the login/signup template with the forms and any errors
    return render(request, "bookings/auth.html", {
        "login_form": login_form,
        "signup_form": signup_form,
        "error_message": error_message,
        # Pass the next URL to template
        "next": next_url  
    })