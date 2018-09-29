#Se debe introducir un termino de una plantilla (ej. Erihplus).
#El programa busca el número que contiene la plantilla, y lo compara con el de Wikidata.
#Si son iguales borra la plantilla.

# -*- coding: utf-8 -*-
from pywikibot import pagegenerators as pg
import pywikibot

#código que busca en la categoría de artículos con la plantilla fusionar y comprueba si el artículo con el que debería fusionarse existe o no. Si no existe se graba en un fichero
def main():
    site = pywikibot.Site("es", "wikipedia")
    wikidata_site = pywikibot.Site("wikidata", "wikidata")
    termino='Latindex'
    propiedad='P3127'
    categoria='Categoría:Wikipedia:Artículos con plantilla '+termino
    cat = pywikibot.Category(site,categoria)
    gen = pg.CategorizedPageGenerator(cat)
    for page in gen:
        print("<<<<<<<<<<<<<<  " + page.title())
        page_str = page.get()
        tmpl_list = pywikibot.textlib.extract_templates_and_params(page_str)
        for tipo in tmpl_list:
            if (termino in tipo):
                  for plantilla in tipo:
                    if (termino in plantilla):
                        continue
                    else:
                        try:
                            item = pywikibot.ItemPage.fromPage(page)
                            dictionary = item.get()
                            lista=item.claims[propiedad][0]
                            if (lista.getTarget()!=plantilla['1']):
                                f = open ("erroresPlantillas.txt", mode='a', encoding='utf-8')
                                f.write(str(page.title()) + '\n')
                                f.close()
                            else:
                                reemplazar="{{" + termino + "|" + plantilla['1'] + "}}"
                                page.text = page.text.replace(reemplazar,'')
                                page.save(u"Ya aparece en control de autoridades")
                        except:
                            f = open ("erroresPlantillas.txt", mode='a', encoding='utf-8')
                            f.write("Exception: " + str(page.title()) + '\n')
                            f.close()
        print ("\n")

if __name__ == "__main__":
    main()
