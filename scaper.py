import requests
from bs4 import BeautifulSoup
import pandas as pd 
from collections import namedtuple
from crear_archivo import crear_archivo
def main(): 
    for i in range(0, 2000, 49):
        url = 'https://listado.mercadolibre.com.ar/computacion/monitores-accesorios/monitores/monitor_Desde_' + str(i) + '_NoIndex_True'
        lista_articulos = web_srap(url)
        crear_archivo(lista_articulos)

def web_srap(url):

    
    Articulo = namedtuple('Articulo', ['nombre', 
                        'precio_antes', 'precio_actual',
                        'descuento', 
                        'url_image'])
    lista_articulos = []

    r = requests.get(url)
    html_contents = r.text

    html_soup = BeautifulSoup(html_contents, 'html.parser')

    articulos_mercado = html_soup.find_all("li",
                                        class_="ui-search-layout__item")

    for articulo in articulos_mercado:
        nombre = articulo.find('h2', class_="ui-search-item__title")
        
        lista_articulos.append(str(nombre))

    return lista_articulos

if __name__ == '__main__':
    main()