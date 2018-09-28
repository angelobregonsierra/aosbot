# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot
import time

#código que busca en la categoría de artículos con la plantilla fusionar y comprueba si el artículo con el que debería fusionarse existe o no. Si no existe se graba en un fichero
def main():
    site = pywikibot.Site("es", "wikipedia")
    cat = pywikibot.Category(site,'Categoría:Wikipedia:Fusionar')
    gen = pg.CategorizedPageGenerator(cat)
    for page in gen:
        print("<<<<<<<<<<<<<<  " + page.title())
        page_str = page.get()
        tmpl_list = pywikibot.textlib.extract_templates_and_params(page_str)
        for tipo in tmpl_list:
            if ("fusionar" in tipo) or ("fusionar en" in tipo) or ("fusionar a" in tipo) or ("fusionar hacia" in tipo) or ("fusionar desde" in tipo)  or ("Fusionar" in tipo):
                  for fus in tipo:
                    if ("fusionar" in fus) or ("Fusionar" in fus):
                       continue
                    else:
                        try:
                            nueva_pagina=pywikibot.Page(site, str(fus['1']))
                            if(nueva_pagina.exists()==False):
                                f = open ("erroresFusionar.txt", mode='a', encoding='utf-8')
                                f.write(str(page.title()) + '\n')
                                f.close()
                        except:
                            f = open ("erroresFusionar.txt", mode='a', encoding='utf-8')
                            f.write('Error en: ' + str(page.title()) + '\n')
                            f.close()
        print ("\n")

if __name__ == "__main__":
    main()
