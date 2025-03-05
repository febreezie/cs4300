from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking



class APITestCases(APITestCase):
    def setUp(self):
        """Set up test data for API testing."""
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Log in the user and store authentication token
        self.client.force_authenticate(user=self.user)  # Ensure requests are authenticated

        self.movie = Movie.objects.create(
            title="Inception",
            description="Dream inside a dream.",
            release_date="2010-07-16",
            duration=148
        )

        self.seat = Seat.objects.create(seat_number="A1", is_booked=False)

    def test_get_movies(self):
        """Test retrieving the list of movies."""
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_seats(self):
        """Test retrieving seat availability."""
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_create_booking(self):
    """Test booking a seat with an authenticated user."""
    self.client.force_authenticate(user=self.user)  # Ensure authentication

    response = self.client.post("/api/bookings/", {
        "movie": self.movie.id,
        "seat": self.seat.id,
        "booking_date": "2025-03-05T12:00:00Z"
    })

    print("DEBUG: Booking response:", response.data)  # Debugging line

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_booking_already_reserved(self):
        """Test trying to book a seat that is already taken."""
        # First Booking
        Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat)
        self.seat.is_booked = True
        self.seat.save()

        self.client.force_authenticate(user=self.user)  # Ensure authentication before request

        # Attempt to Book Again
        response = self.client.post("/api/bookings/", {
            "user": self.user.id,  # Explicitly pass user ID
            "movie": self.movie.id,
            "seat": self.seat.id,
            "booking_date": "2025-03-05T12:00:00Z"
        })

        print("DEBUG: Booking response:", response.data)  # Debugging line

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
