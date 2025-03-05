
#3.5 RESTful API Implementation 

from rest_framework import serializers
from .models import Movie, Seat, Booking


#Converts movie model to JSON format for API response
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

#Converts seat model to JSON format for API response
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

#Converts booking model to JSON format for API response
class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    movie = serializers.StringRelatedField()
    seat = serializers.StringRelatedField()

    class Meta:
        model = Booking
        fields = '__all__'

    #Assigns the user a booking, associatesz booking to authenticated user
    def create(self, validated_data):
        """Ensure the user is assigned from the request."""
        request = self.context.get("request")  
        validated_data["user"] = request.user  
        return super().create(validated_data)
