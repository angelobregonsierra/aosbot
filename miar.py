# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot
from bs4 import BeautifulSoup
from urllib.request import urlopen

def preparar(url):
    req = urlopen(url)
    soup = BeautifulSoup(req.read(),"html.parser")
	#controlamos que la clase badge tiene un valor dentro, si es 0 registros entonces no existe esa página
    try:
        resultado=str(soup.find_all("span", "badge"))
        resultado=resultado.split(">")
        resultado=resultado[1].split(" ")
        if(resultado[0]=="0"):
            #print('Este ISSN no tiene página en MIAR')
            return 0
        else:
            #print('Este ISSN tiene página en MIAR, aquí: ' + url)
            return 1
    except:
        #con ciertas páginas no puede encontrar badge porque es exitosa y no tiene la clase badge
        #print('Este ISSN tiene página en MIAR, aquí: ' + url)
        return 1

def cambiar(q):
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, q)
    item.get()
    #Pongo el mismo formato que tendrá page cuando les comparo en el if
    nombre='[[wikipedia:es:' + str(item.sitelinks['eswiki']) + "]]"
    site2 = pywikibot.Site('es', 'wikipedia')
    cat2 = pywikibot.Category(site2,'Categoría:Wikipedia:Artículos con plantilla MIAR')
    gen = pg.CategorizedPageGenerator(cat2)
    cont=0
    for page in gen:
        if (nombre==str(page)):
            #Si entra aquí el artículo de wikidata que analizamos está en la categoría, no necesita {{miar}}
            print(str(page) + ' ya tiene la etiqueta {{MIAR}}')
            cont=1
            break
    if (cont==0):
        #No está en la categoría, tenemos que añadir {{miar}}
        #page = pywikibot.Page(site, str(item.sitelinks['eswiki']))
        #page.text = u"{{MIAR}}"
        #page.save(u"Aosbot añadiendo la etiqueta MIAR")
        print('>>>>Se añadido la plantilla MIAR a ' + nombre)
		
def consulta(site=None):
    #Devuelve la consulta que necesitamos, los items con issn que tienen artículo en español
    query = """ SELECT ?item ?itemLabel ?ISSN WHERE {
        ?item wdt:P31 wd:Q5633421.
        ?item wdt:P236 ?ISSN.
		?article schema:about ?item.
        ?article schema:isPartOf <https://es.wikipedia.org/>.
        ?article schema:name ?page_titleRO.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],es". }
    } """
    #print(query)
    return pg.WikidataSPARQLPageGenerator(query, site=site)

def issn(repo,item):
    #print ('>>> La revista que está en ' + item + ' tiene este issn: ')
    articulo = pywikibot.ItemPage(repo, item)
    articulo.get()
    sourcesid = 'P236'
    if sourcesid in articulo.claims:
        for source in articulo.claims[sourcesid]:
            return(source.target)
			
if __name__ == "__main__":
    site = pywikibot.Site("wikidata", "wikidata")
    repo = site.data_repository()
    pages = consulta(site)
    for item in pages:
	    #no sé como obtener el Q, por eso lo paso a string y lo corto hasta coger el Q entero
        item=str(item)
        item=item.split(":")
        item=item[1].split("]")
		#llamo a la función que me devuelve el issn del item
        codigo=issn(repo,item[0])
        url = 'http://miar.ub.edu/issn/'+codigo
        if (preparar(url)):
            cambiar(item[0])