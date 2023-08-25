import requests
from bs4 import BeautifulSoup
import time

# URL del sitio web que deseas analizar
url = 'https://www.bna.com.ar'

respuesta= requests.get(url)
contenidoHTML=respuesta.content

soup = BeautifulSoup(contenidoHTML, 'html.parser')

cuerpo=soup.body

ver=cuerpo.find_text(id="billetes")
print(ver)