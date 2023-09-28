import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
peticion = requests.get(url)

if peticion.status_code == 200:
    # Lee la imagen desde la respuesta HTTP
    imagen = Image.open(BytesIO(peticion.content))

    imagen_bgr = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)
    # Convierte la imagen de RGB a BGR

    # Divide la imagen en canales de color (BGR)
    b, g, r = cv2.split(imagen_bgr)

    # Muestra los canales por separado
    cv2.imshow('azul', b)
    cv2.imshow('verde', g)
    cv2.imshow('rojo', r)

    cv2.waitKey(0)
else:
    print("La solicitud no fue exitosa. Código de estado:", peticion.status_code)
