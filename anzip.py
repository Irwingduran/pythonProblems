from geopy.geocoders import Nominatim

# Create the geolocator object with a user-agent
geolocator = Nominatim(user_agent="geoapiExercises")

# Get the city name
place = input("Enter city name: ")

# Geocode the location

location = geolocator.geocode(place)

print(location)
