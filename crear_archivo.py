import pickle
from django.utils.html import strip_tags
def clear_Html(txt):
    return strip_tags(txt)


def crear_archivo(lista_articulos):
    nombre = 'articulos.csv'
    archivo = open(nombre, 'a+t')

    for articulo in lista_articulos:
        articulo = articulo + "\n"
        articulo = clear_Html(articulo)
        archivo.write(articulo)
        
    archivo.close()
