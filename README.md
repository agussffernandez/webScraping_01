# Web Scraping de Máquinas Dockerlabs

Este script realiza un web scraping en la página dockerlabs.es, para extraer y procesar información sobre máquinas disponibles. Extrae el nombre, dificultad y autor de cada máquina listada en la página, y finalmente muestra los resultados.

# Funcionalidad 
* Realiza una petición HTTP GET a la URL proporcionada.
* Extrae la información relevante de cada máquina (nombre, dificultad y autor) utilizando el módulo BeautifulSoup para analizar el HTML.
* Imprime en consola el nombre, dificultad y autor de cada máquina encontrada.
* Muestra el número total de máquinas encontradas.

# Requisitos
Para ejecutar este script, debes tener las siguientes bibliotecas instaladas:

-> requests: Para realizar la petición HTTP.

-> beautifulsoup4: Para analizar y extraer información del HTML de la página web.

Si no tienes estas bibliotecas instaladas, puedes hacerlo ejecutando el siguiente comando:
pip install requests beautifulsoup4
