# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot

categories_fusionar = ['fusionar en', 'fusionar a',
                       'fusionar hacia', 'fusionar desde', 'fusionar']


def write(data='', file='fusionar.txt'):
    f = open(file, "a", encoding='utf8')
    f.write(data + '\n')
    f.close()

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
                write(data='[!!] Falta parámetro en {0}'.format(
                    str(page.title())))
                continue
            else:
                try:
                    nueva_pagina = pywikibot.Page(site, str(parametros['1']))
                    if(nueva_pagina.exists() == False):
                        write(data=str(page.title()))
                    else:
                        print('La página {0} existe'.format(
                            nueva_pagina.title()))
                except Exception:
                    write(data='[!] Error en {0}'.format(str(page.title())))


if __name__ == "__main__":
    main()
