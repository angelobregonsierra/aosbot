#Busca en una categoría dada todos los artículos para saber si tiene la plantilla defaultsort
#Si la encuentra busca si tiene NF, en ese caso debe borrarse

# -*- coding: utf-8 -*-
from pywikibot import pagegenerators as pg
import pywikibot

def main():
    site = pywikibot.Site("es", "wikipedia")
    wikidata_site = pywikibot.Site("wikidata", "wikidata")
    categoria='Categoría:Personas'
    cat = pywikibot.Category(site,categoria)
    gen = pg.CategorizedPageGenerator(cat, recurse=True)
    for page in gen:
        print(page.title())
        page_str = page.get()
        tmpl_list = pywikibot.textlib.extract_templates_and_params(page_str)
        for tipo in tmpl_list:
            if ("DEFAULTSORT" in tipo) or ("Defaultsort" in tipo) or ("defaultsort" in tipo) or ("DefaultSort" in tipo):
                try:
                    item = pywikibot.ItemPage.fromPage(page)
                    print("<<<<<<<<<<<<<<  " + page.title())
                    f = open ("erroresDefaultSort.txt", mode='a', encoding='utf-8')
                    f.write(str(page.title()) + '\n')
                    f.close()
                except:
                    f = open ("erroresDefaultsort.txt", mode='a', encoding='utf-8')
                    f.write("Exception: " + str(page.title()) + '\n')
                    f.close()

if __name__ == "__main__":
    main()
