import requests
from bs4 import BeautifulSoup

def obtener_respuesta(url):
    """
    Realiza una petición GET a la URL y retorna el contenido HTML si es exitoso.
    
    Args:
        url(str): cadena de texto de la url a obtener respuesta
        
    Return:
    
    """
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.text
    else:
        print("Hubo un error al hacer la petición")
        return None

def procesar_maquinas(maquinas: list):
    """
    Procesa las máquinas encontradas en el HTML y extrae la información relevante.
    
    Args:
        maquinas(list): Lista con las maquinas
    
    Return:
        (list,int): Tupla con una lista con cada info de cada maquina y la cantidad de maquinas
        
    """
    maquinas_info = [] # Lista para almacenar la información de las máquinas
    conteo_maquinas = 0
    
    for maquina in maquinas:
        onclick_text = maquina["onclick"]
        nombre_maquina = onclick_text.split("'")[1]
        dificultad = onclick_text.split("'")[3]
        autor = onclick_text.split("'")[7]
        maquinas_info.append((nombre_maquina, dificultad, autor))
        conteo_maquinas += 1
    
    return maquinas_info, conteo_maquinas

def imprimir_resultados(maquinas_info, conteo_maquinas):
    """
    Imprime los el nombre de cada máquina con su dificultas y autor. 
    Y la cantidad de máquinas encontradas.
    """
    for nombre_maquina, dificultad, autor in maquinas_info:
        print(f"{nombre_maquina} --> {dificultad} --> {autor}")
    
    print(f"El nro de máquinas encontradas es: {conteo_maquinas}")

def main():
    url = "http://dockerlabs.es"
    html = obtener_respuesta(url)
    
    if html:
        soup = BeautifulSoup(html, "html.parser")
        maquinas = soup.find_all("div", onclick=True)
        maquinas_info, conteo_maquinas = procesar_maquinas(maquinas)
        imprimir_resultados(maquinas_info, conteo_maquinas)

main()