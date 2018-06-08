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
    with open(archivo, encoding="utf8") as f:
        for line in f.readlines():
            data.append(line.split(separador))
    return data


def cambiar(item, descripcion):
    """
    cambiar(item, descripcion):
        Cambia un item en Wikidata con la descripcion entregada
    """
    print(item)
    mydescriptions = {u'es': u''+ descripcion +''}
    item.editDescriptions(mydescriptions, summary=u'Actualizando descripción con aosbot.')

def consulta(qprofesion, qpais, sexo, site=None):
    """
    consulta(qprofesion, qpais, sexo):
        Devuelve la consulta que necesitamos en cada momento
    """
    # qpais[0]=q de wikidata  qpais[1]=país  qpais[2]=toponimo masc  qpais[3]=toponimo fem
    query = """
    SELECT ?item ?gender WHERE {
      ?item wdt:P106 wd:""" + qprofesion + """.
      ?item wdt:P27 wd:""" + qpais + """.
      ?item wdt:P21 wd:""" + sexo + """.
    OPTIONAL {
    ?item schema:description ?description.
    FILTER((LANG(?description)) = "es")
      }
      FILTER(NOT EXISTS {
    ?item wdt:P106 ?occupation.
    FILTER(?occupation != wd:""" + qprofesion + """)
      })
      FILTER(NOT EXISTS {
    ?item wdt:P27 ?occupation.
    FILTER(?occupation != wd:""" + qpais + """)
      })
      FILTER(!BOUND(?description))
    } """
    #print(query)
    return pg.WikidataSPARQLPageGenerator(query, site=site)


def main():
    wikidata_site = pywikibot.Site("wikidata", "wikidata")
    profesiones = obtener_data('profesiones.txt')
    for profesion in profesiones:
        if len(profesion) != 3:
            continue
        qProfesion, profesion_mas, profesion_fem = profesion
        toponimos = obtener_data('toponimos.txt')
        for toponimo in toponimos:
            if len(toponimo) != 4:
                continue
            qToponimo, toponimo_pais, toponimo_mas, toponimo_fem = toponimo
            for i in [0,1]:
                genero = FEM if i % 2 else MAS
                profesion_gen = profesion_fem if i % 2 else profesion_mas
                toponimo_gen = toponimo_fem if i % 2 else toponimo_mas
                profesion_gen=profesion_gen.rstrip('\n')
                toponimo_gen=toponimo_gen.rstrip('\n')
                descripcion = "{0} {1}".format(profesion_gen, toponimo_gen)
                print ('>>> Consultando {0}'.format(descripcion))
                pages = consulta(qProfesion, qToponimo, genero, site=wikidata_site)
                for item in pages:
                    cambiar(item, descripcion)
                    print('Pausando 20 segundos...')
                    time.sleep(20)


if __name__ == "__main__":
    main()
