# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot

# código que busca en la categoría de páginas con palabras mágicas mal usadas y cambia el | por el :
def main():
    site = pywikibot.Site("es", "wikipedia")
    cat = pywikibot.Category(site, 'Categoría:Wikipedia:Páginas con palabras mágicas mal usadas')
    gen = pg.CategorizedPageGenerator(cat, namespaces=[0, 100])
    articles = pg.PreloadingGenerator(gen)
    for page in articles:
        print("<<<<<<<<<<<<<< {0} ".format(page.title()))
        page_str = page.get()
        tmpl_list = pywikibot.textlib.extract_templates_and_params(page_str)
        for tipo in tmpl_list:
            if "ORDENAR" in tipo:
                page_new=page_str.replace("ORDENAR|", "ORDENAR:")
                page.put(page_new, "Cambiando | por : en palabra mágica")
            if "PAGENAME" in tipo:
                page_new=page_str.replace("PAGENAME|", "PAGENAME:")
                page.put(page_new, "Cambiando | por : en palabra mágica")


if __name__ == "__main__":
    main()
