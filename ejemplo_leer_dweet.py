# Este programa muestra como leer un dweet.

import requests
import json

peticion = "https://dweet.io/get/dweets/for/mi-cosa-2017-10"
respuesta = requests.get(peticion)

if respuesta.status_code == 200:
    objeto_json = json.loads(respuesta.text)
    contenido = objeto_json["with"][0]["content"]
    temp = int(contenido["temperatura"])
    lumi = float(contenido["luminosidad"])
    print "Temperatura =", temp
    print "Luminosidad =", lumi
else:
    print "Hubo un error."
    print respuesta.status_code
