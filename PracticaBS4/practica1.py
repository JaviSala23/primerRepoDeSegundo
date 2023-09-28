
from bs4 import BeautifulSoup as Bs
import requests as rq


url="https://www.google.com" #url objetivo


try:  
    respuesta = rq.get(url) #utilizamos rq (requests) para pedir el html de la pagina
    sopa = Bs(respuesta.text,'html.parser') #creamos un objeto con la respuesta y pasando el formato
    resultadoBusqueda=sopa.find('a')
   
    
    link=resultadoBusqueda['href']

    try:
        imagen=rq.get(link)
        if imagen.status_code == 200:
            respuestaImagen=Bs(imagen.text,'html.parser')
            resultadoImg=respuestaImagen.find_all('meta')
            img=resultadoImg[2]['content']
         
            link1=url+'/'+img
            print(link1)
            imagen1=rq.get(link1)
            
           
            
            
            
            
            
        # Acceder al contenido de la respuesta
            contenido_binario=imagen1.content
            ruta_guardado = "googlelogo.png"

        # Abre el archivo en modo escritura y guarda el contenido de la respuesta en él
        with open(ruta_guardado, "wb") as archivo:
            archivo.write(contenido_binario)
            
    except rq.exceptions.RequestException as e :
        print(f"Error al descargar imagen")
    
    
    
except rq.exceptions.RequestException as e :
    print(f"Error al descargar pagina")





