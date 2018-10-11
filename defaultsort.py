# Busca en una categoría dada todos los artículos para saber si tiene la plantilla defaultsort
# Si la encuentra busca si tiene NF, en ese caso debe borrarse

# -*- coding: utf-8 -*-
from pywikibot import pagegenerators as pg
import pywikibot
import aosbot as tools

site = pywikibot.Site("es", "wikipedia")


def main(*args):

    category = 'Personas'
    local_args = pywikibot.handle_args(args)
    for arg in local_args:
        if arg.startswith('-category:'):
            category = arg[10:]

    cat = pywikibot.Category(site, 'Category:' + category)
    gen = pg.CategorizedPageGenerator(cat, recurse=True)
    articles = pg.PreloadingGenerator(gen)
    for page in articles:
        if page.isRedirectPage() or page.namespace() != 0:
            continue
        print('>>> {0}'.format(page.title()))
        templates = pywikibot.textlib.extract_templates_and_params(page.get())
        categories = page.categories()

        isHuman = list(filter(lambda x: x.title(with_ns=False).lower() in [
                       'mujeres', 'hombres'], categories))
        hasNF = list(
            filter(lambda x: x[0].lower() in ['nf', 'bd'], templates))
        hasDefaultSort = list(
            filter(lambda x: x[0].lower().find('defaultsort') > -1 or x[0].lower().find('ordenar') > -1, templates))
        hasFicha = list(filter(lambda x: x[0].lower().find(
            'ficha de') > -1, templates))

        if (not len(hasFicha) or not len(isHuman)) and not len(hasNF):
            """ Presumiblemente no es humano """
            continue
        if len(hasNF) and len(hasDefaultSort):
            string = "[!!]\t{0}\ttiene DEFAULTSORT y NF".format(page.title())
            tools.write(string, 'defaultsort.txt')
        if len(hasDefaultSort) and not len(hasNF):
            """ Tiene defaultsort, pero no NF """
            string = "[?]\t{0}\ttiene solo DEFAULTSORT".format(page.title())
            tools.write(string, 'defaultsort.txt')
        if not len(hasDefaultSort) and not len(hasNF):
            """ No tiene ni fu ni fa """
            string = "[??]\t{0}\tno tiene clave de ordenamiento".format(
                page.title())
            tools.write(string, 'defaultsort.txt')


if __name__ == "__main__":
    main()
