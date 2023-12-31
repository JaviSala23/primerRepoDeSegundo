import requests as rq
from bs4 import BeautifulSoup as bs
import sqlite3
from modelos import * 
import funciones
import time

# Calcula el número de segundos en un día
un_dia_en_segundos = 24 * 60 * 60  # 24 horas * 60 minutos/hora * 60 segundos/minuto

# Duerme durante 1 día


while True:
   bd=BaseDatos()
   bd.generarTablas()

   url="https://quinielanacional1.com.ar/"
   pagina=rq.get(url)
   sopa=bs(pagina.text,'html.parser')
   menuFecha=sopa.find(id='menu')
   fechaAproxi=menuFecha.find('h2')
   fecha=funciones.formatearFecha(fechaAproxi.text)
   encontrada= bd.encontrarFecha(fecha)

   if not encontrada:
      ultimaFecha=bd.crearFecha(fecha)
      
      columnas=sopa.find_all('div', class_='columna')

      for columna in columnas:
         
         titulo=columna.find('p')
         
         tituloEncontrado=bd.encontrarTitulo(titulo.text)#tituloEncontrado es == id de quinela
         veitenas=columna.find_all('div',class_='veintena')
         for veitena in veitenas:
            cantidadDiv=veitena.find_all('div')
            i=0
            for cantidad in cantidadDiv:
               if i%2 == 0:
                  posicion=bd.encontrarPosicion(cantidad.text)
               else:
                  bd.guardarNumero(ultimaFecha[0],posicion[0],tituloEncontrado[0],int(cantidad.text))
               i=i+1
               
   time.sleep(un_dia_en_segundos)