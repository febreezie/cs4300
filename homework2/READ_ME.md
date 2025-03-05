#Homework 2: Django Tutorial

You are tasked with building a RESTful Movie Theater Booking Application using Python and
Django. The application should allow users to:

• View movie listings via the API

• Book seats via the API

• Check their booking history via the API

• An attractive user interface using Django templates and Bootstrap that displays and manipulates the same data as the API.

## Getting Started
### **Navigate to the Project Directory**

```bash
cd cs4200
cd homework2
cd movie_theater_booking
```
 **Opening Environment**
```bash
python3 -m venv myenv -- system - site - packages
source myenv / bin / activate
pip install django djangorestframework
```
**Do Migrations**
```bash
python manage.py makemigrations bookings
python manage.py migrate
python manage.py runserver 0.0.0.0:3000
```
**Creating a Fake Movie Database**
```bash
python manage.py shell
```

**Copy into Shell**
```bash
from bookings.models import Movie, Seat

# Create Fake Movies
movie1 = Movie.objects.create(title="The Matrix", description="A sci-fi classic", release_date="1999-03-31", duration=136)
movie2 = Movie.objects.create(title="Inception", description="A mind-bending thriller", release_date="2010-07-16", duration=148)
movie3 = Movie.objects.create(title="Avatar", description="A visually stunning sci-fi epic", release_date="2009-12-18", duration=162)

# Function to create seats for a movie
def create_seats(movie, total_seats=10):
    for i in range(1, total_seats + 1):
        Seat.objects.create(seat_number=f"{movie.title[:3].upper()}-S{i}", is_booked=False)

# Create seats for each movie
for movie in Movie.objects.all():
    create_seats(movie)

# Verify Data
print("Movies Created:", Movie.objects.all())
print("Seats Created:", Seat.objects.all())
```

**Testing**
```bash
python manage.py test bookings
```


## OPENAI HELP:

**3.2**:

-Help with how to connect models for django.

-Explains what on_delete=models.CASCADE does.

-Help with how to use django user feature/what it does.

**3.3:**

-Commands to Run migrations for django

-Explaining what DJANGO RESTFUL viewset is

-Explain Meta and other various syntax

-How to use views.py and what to import

**3.5**
-Asked to explain what prompt is asking

**General**

Mostly used for general trouble shooting, however was not much help and often wrong.

**LINK**
https://chatgpt.com/share/67c7d8ed-6b30-8012-a077-11f688709274