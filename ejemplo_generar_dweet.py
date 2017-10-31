# Este programa muestra como escribir un dweet.

import requests
import json

temp = 17.3
lumi = 230

query = "temperatura=" + str(temp) + "&luminosidad=" + str(lumi)
peticion = "https://dweet.io/dweet/for/mi-cosa-2017-10?" + query
respuesta = requests.get(peticion)

if respuesta.status_code == 200:
    print "Todo bien."
    print
    print "Ok"
    objeto = json.loads(respuesta.text)
    print objeto["this"]
    print objeto["with"]["thing"]
    print 
else:
    print "Hubo un error."
    print respuesta.status_code
