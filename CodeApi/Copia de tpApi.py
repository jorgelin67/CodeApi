import requests
import subprocess

class Clima:
    def __init__(self):
        self.ciudad = "Villa Diamante, AR"
        self.apiKey = "9c4730fe91d05c5aa1184d90adb5d425"

    def obtenerClima(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.ciudad}&appid={self.apiKey}"
        response = requests.get(url)
        datosClima = response.json()
        temperatura = datosClima["main"]["temp"]
        humedad = datosClima["main"]["humidity"]
        descripcion = datosClima["weather"][0]["description"]

        return temperatura, humedad, descripcion

climaActual = Clima()

temperatura, humedad, descripcion = climaActual.obtenerClima()

#def traducir(oracion, idioma):
#    comando = f"trans -b :{idioma} '{oracion}'"
#    traducido = subprocess.check_output(comando, shell=True).decode("utf-8").strip()
#    return traducido

#idioma = "es"  # Código ISO del idioma destino, "es" corresponde a español
#traducido = traducir(descripcion, idioma) "Sacado de internet"

print("Datos del clima en:", climaActual.ciudad.upper())
a= temperatura-273
b= a//1
print("Temperatura:", b,"º", "Grados Celsius")
print("Humedad:",humedad, "%")
print("Descripcion:",descripcion.capitalize())
#print("Descripcion:",traducido.capitalize())