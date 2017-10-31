# Este programa muestra como realizar una peticion.

import requests

respuesta = requests.get('https://www.google.com/')

print respuesta.status_code
print respuesta.text
