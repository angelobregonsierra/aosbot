#Se buscan personas que no tengan ficha dependiendo de la temática y se pone el tipo de ficha que necesiten

# -*- coding: utf-8 -*-
from pywikibot import pagegenerators as pg
import pywikibot

def obtener_data(archivo, separador="\n"):
    """
    obtener_data(archivo, separador="\n"):
        Obtiene los contenidos del archivo que usa el separador \t
    """
    data = []
    with open(archivo, encoding="utf-8") as f:
        for line in f.readlines():
            cortada=line.split(separador)
            data.append(cortada[0])
    return data

def main():
    site = pywikibot.Site("es", "wikipedia")
    termino='Medallistas paralímpicos de México'
    categoria='Categoría:'+termino
    fichas=obtener_data('../aosbot/fichas.txt')
    cat = pywikibot.Category(site,categoria)
    gen = pg.CategorizedPageGenerator(cat, recurse=True)
    cont=0
    for page in gen:
        print("<<<<<<<<<<<<<<  " + page.title())
        try:
            item = pywikibot.ItemPage.fromPage(page)
            dictionary = item.get()
            lista=item.claims['P31'][0].getTarget()
            if(str(lista)=='[[wikidata:Q5]]'):
                page_str = page.get()
                tmpl_list = pywikibot.textlib.extract_templates_and_params(page_str)
                for tmpl in tmpl_list:
                    for ficha in fichas:
                        if ficha in tmpl:
                           cont=cont+1
                           break
                if (cont==0):
                    limit=page.text
                    print(limit[0:500])
                    choice = pywikibot.input_choice(u'Introduce el número de la ficha que quieres introducir u otra cosa para pasar a otro artículo',
					[('Ficha de persona','1'),('Ficha de deportista','2'),('Ficha de actor','3')])
                    if choice == '1':
                        escribe="{{Ficha de persona}}\n"+page.text
                        page.put(escribe, comment="Introduciendo ficha")
                    elif choice == '2':
                        escribe="{{Ficha de deportista}}\n"+page.text
                        page.put(escribe, comment="Introduciendo ficha")
                    elif choice == '3':
                        escribe="{{Ficha de actor}}\n"+page.text
                        page.put(escribe, comment="Introduciendo ficha")
                    else: 
                        break
            cont=0
        except:
            f = open ("erroresFichas.txt", mode='a', encoding='utf-8')
            f.write('Error en: ' + str(page.title()) + '\n')
            f.close()


if __name__ == "__main__":
    main()
