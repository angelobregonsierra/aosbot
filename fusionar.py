# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot
import aosbot as tools

categories_fusionar = ['fusionar en', 'fusionar a',
                       'fusionar hacia', 'fusionar desde', 'fusionar']


# código que busca en la categoría de artículos con la plantilla fusionar y comprueba si el artículo con el que debería fusionarse existe o no. Si no existe se graba en un fichero

def main():
    site = pywikibot.Site("es", "wikipedia")
    cat = pywikibot.Category(site, 'Categoría:Wikipedia:Fusionar')
    gen = pg.CategorizedPageGenerator(cat, namespaces=[0, 100])
    articles = pg.PreloadingGenerator(gen)
    for page in articles:
        print("<<<<<<<<<<<<<< {0} ".format(page.title()))
        page_str = page.get()
        tmpl_list = pywikibot.textlib.extract_templates_and_params(page_str)
        templates_to_check = filter(
            lambda x: x[0].lower() in categories_fusionar, tmpl_list)
        for tipo in templates_to_check:
            plantilla, parametros = tipo
            if '1' not in parametros:
                tools.write(data='[!!] Falta parámetro en {0}'.format(
                    str(page.title())), filename="fusionar.txt")
                continue
            else:
                try:
                    nueva_pagina = pywikibot.Page(site, str(parametros['1']))
                    if(nueva_pagina.exists() == False):
                        tools.write(data=str(page.title()),
                                    filename="fusionar.txt")
                    else:
                        print('La página {0} existe'.format(
                            nueva_pagina.title()))
                except Exception:
                    tools.write(data='[!] Error en {0}'.format(
                        str(page.title())), filename="fusionar.txt")


if __name__ == "__main__":
    main()
