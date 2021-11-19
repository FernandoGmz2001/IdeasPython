import phonenumbers
import folium
from minumero import numero
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

Key = '4e45732b2fdb412b84f53e8184c23907'

Numeros = phonenumbers.parse(numero)
Localizacion = geocoder.description_for_number(Numeros,"es")
print(Localizacion)
#<------------------------------Conocer el proveedor de servicio--------------------------------->
# ProveedorServicio = phonenumbers.parse(numero)
# print(carrier.name_for_number(ProveedorServicio,"es"))

#<---------------------------------Conocer latitud y longitud------------------------------------>
geocoder = OpenCageGeocode(Key)
consulta = str(Localizacion)
resultado = geocoder.geocode(consulta)

lat = resultado[0]['geometry']['lat']
lng = resultado[0]['geometry']['lng']

print(lat,lng)

miMapa= folium.Map(location=[lat,lng],zoom_start = 9)
folium.Marker([lat,lng],popup=Localizacion).add_to((miMapa))


#<-------------------------------------Guardar mapa en html-------------------------------------->
miMapa.save("Localizacion.html")

