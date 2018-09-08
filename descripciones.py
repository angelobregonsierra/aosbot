# -*- coding: utf-8 -*-

from pywikibot import pagegenerators as pg
import pywikibot
import time

FEM = 'Q6581072'
MAS = 'Q6581097'

def obtener_data(archivo, separador="\t"):
    """
    obtener_data(archivo, separador="\t"):
        Obtiene los contenidos del archivo que usa el sparador \t
    """
    data = []
    with open(archivo, encoding="utf-8") as f:
        for line in f.readlines():
            data.append(line.split(separador))
    return data


def cambiar(item, descripcion):
    """
    cambiar(item, descripcion):
        Cambia un item en Wikidata con la descripcion entregada
    """
    print(item)
    summary=u'Se añaden descripciones en varios idiomas'
    try:
        item.get();
        for cod_idioma in item.descriptions:
            if(cod_idioma in descripcion):
                del descripcion[cod_idioma]
        item.editDescriptions(descripcion, summary=summary)
    except:
        f = open ("errores.txt", "a")
        f.write(str(item) + '\n')
        f.close()
        print ('No se ha podido modificar la descripción de: ' + str(item))

	
def consulta(qprofesion, qpais, sexo, site=None):
    """
    consulta(qprofesion, qpais, sexo):
        Devuelve la consulta que necesitamos en cada momento
    """
    # qpais[0]=q de wikidata  qpais[1]=país  qpais[2]=toponimo masc  qpais[3]=toponimo fem
    query = """
    SELECT DISTINCT ?item ?gender WHERE {
      ?item wdt:P106 wd:""" + qprofesion + """.
      ?item wdt:P27 wd:""" + qpais + """.
      ?item wdt:P21 wd:""" + sexo + """.
    {
        FILTER (NOT EXISTS {
          ?item schema:description ?description.
          FILTER((LANG(?description)) = "es")
        })
    }
    UNION 
    {
        FILTER (NOT EXISTS {
           ?item schema:description ?description.
           FILTER((LANG(?description)) = "ast")
        })
    }
    FILTER(NOT EXISTS {
       ?item wdt:P106 ?occupation.
       FILTER(?occupation != wd:""" + qprofesion + """)
    })
    FILTER(NOT EXISTS {
      ?item wdt:P27 ?pais.
      FILTER(?pais != wd:""" + qpais + """)
    })
    FILTER(!BOUND(?description))
      FILTER(NOT EXISTS { ?item wdt:P31 wd:Q95074. })
      FILTER(NOT EXISTS { ?item wdt:P31 wd:Q15632617. })
    } """
    #print(query)
    return pg.WikidataSPARQLPageGenerator(query, site=site)


def main():
    wikidata_site = pywikibot.Site("wikidata", "wikidata")
    profesiones = obtener_data('../aosbot/profesiones.txt')
    for profesion in profesiones:
        if len(profesion) != 5:
            continue
        qProfesion, profesion_mas, profesion_fem, profesion_mas_ast, profesion_fem_ast= profesion
        toponimos = obtener_data('../aosbot/gentilicios.txt')
        for toponimo in toponimos:
            if len(toponimo) != 6:
                continue
            qGentilicio, gentilicio_pais, gentilicio_mas, gentilicio_fem, gentilicio_mas_ast, gentilicio_fem_ast = toponimo
            for i in [0,1]:
                genero = FEM if i % 2 else MAS
                profesion_es = profesion_fem if i % 2 else profesion_mas
                gentilicio_es = gentilicio_fem if i % 2 else gentilicio_mas
                profesion_ast = profesion_fem_ast if i % 2 else profesion_mas_ast
                gentilicio_ast = gentilicio_fem_ast if i % 2 else gentilicio_mas_ast
                profesion_es=profesion_es.rstrip('\n')
                gentilicio_es=gentilicio_es.rstrip('\n')
                profesion_ast=profesion_ast.rstrip('\n')
                gentilicio_ast=gentilicio_ast.rstrip('\n')
                descripcion = {u'es': u''+ "{0} {1}".format(profesion_es, gentilicio_es) +'', u'ast': u''+ "{0} {1}".format(profesion_ast, gentilicio_ast)}
                print ('>>> Consultando {0} {1}'.format(profesion_es, gentilicio_es))
                pages = consulta(qProfesion, qGentilicio, genero, site=wikidata_site)
                for item in pages:
                    cambiar(item, descripcion)
                    #print('Pausando 10 segundos...')
                    #time.sleep(10)


if __name__ == "__main__":
    main()
