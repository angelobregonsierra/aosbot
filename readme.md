# AOSBOT

`descripciones.py` -> Es un script para introducir en Wikidata las descripciones de personas con un trabajo concreto y procedentes de un único país, por ejemplo "cantante estadounidense".

`miar.py` -> Es un script para revisar aquellas revistas que están en Wikidata con ISSN y con artículo en español pero que dentro del artículo no tienen la plantilla `{{MIAR}}`. En caso de ser así la añade.

`defaultsort.py` -> Es un script que busca en una determinada categoría (defecto [Categoría:Personas](https://es.wikipedia.org/wiki/Category:Personas)) si están las plantillas [`NF`](https://es.wikipedia.org/wiki/Template:NF) o la palabra mágica `DEFAULTSORT` (y sus traducciones al español)

# Requisitos
* `pywikibot`
* `python3`
