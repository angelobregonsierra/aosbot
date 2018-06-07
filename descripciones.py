import pywikibot
from pywikibot import pagegenerators as pg
	
#Para cambiar el elemento de Wikidata
def cambiar(item, descripcion, qwikidata):
	#time.sleep(10)
	#repo = wikidata_site.data_repository()
	#item = pywikibot.ItemPage(repo, qwikidata)
	#item.get()
	print(item)
	#mydescriptions = {u'es': u''+ descripcion +''}
	#print(mydescriptions)
	#item.editDescriptions(mydescriptions, summary=u'Actualizando descripción con aosbot.')

#Devuelve la consulta que necesitamos en cada momento
def consulta (qprofesion,qpais,sexo):
	#qpais[0]=q de wikidata  qpais[1]=país  qpais[2]=toponimo masc  qpais[3]=toponimo fem
	query = """
	SELECT ?item ?gender WHERE {
	  ?item wdt:P106 wd:""" + qprofesion[0] + """.
	  ?item wdt:P27 wd:""" + qpais[0] + """.
	  ?item wdt:P21 wd:""" + sexo + """.
	OPTIONAL {
		?item schema:description ?description.
		FILTER((LANG(?description)) = "es")
	  }
	  FILTER(NOT EXISTS {
		?item wdt:P106 ?occupation.
		FILTER(?occupation != wd:""" + qprofesion[0] + """)
	  })
	  FILTER(NOT EXISTS {
		?item wdt:P27 ?occupation.
		FILTER(?occupation != wd:""" + qpais[0] + """)
	  })
	  FILTER(!BOUND(?description))
	} """
	#print(query)
	return query

def main():
	g = open('profesiones.txt')
	#bucle para recorrer el fichero de las profesiones
	for lineaprofesion in g:
		qprofesion=lineaprofesion.split("	")
		f = open('toponimos.txt')
		#bucle para recorrer el fichero de países y topónimos
		for lineapais in f:
			qpais=lineapais.split("	")
			genero=0
			#bucle de dos iteraciones para cambiar el género
			while genero != 2:
				if genero == 0:
					sexo="Q6581097"
					profesion=qprofesion[1]
				else:
					sexo="Q6581072"
					profesion=qprofesion[2]
				profesion=profesion.rstrip('\n')
				qpais[3]=qpais[3].rstrip('\n')
				if genero==0:
					descripcion=profesion + " " + qpais[2]
				else:
					descripcion=profesion + " " + qpais[3]
				descripcion.rstrip('\n')
				print (descripcion)
				
				query = consulta(qprofesion,qpais,sexo)
				wikidata_site = pywikibot.Site("wikidata", "wikidata")
				generator = pg.WikidataSPARQLPageGenerator(query, site=wikidata_site)
				for item in generator:
					cambiar (item, descripcion, qpais[0])
				genero=genero+1
		f.close()
		
if __name__ == "__main__":
    main()
