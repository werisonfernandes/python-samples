# -** encoding: utf-8
from geopy.geocoders import Nominatim
from Functions.JsonFunctions import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes")
dicionario = ler_arquivo("../Temp/entrada.json")
lista = dicionario["endereco"]
endereco = lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
saida = {"coordenadas": (location.latitude, location.longitude)}
gravar_arquivo(saida, "../Temp/saida.json")