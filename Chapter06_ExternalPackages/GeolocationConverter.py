# -** encoding: utf-8
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
location = geolocator.geocode("Rua anibal freire")
print(location.address)
print((location.latitude, location.longitude))