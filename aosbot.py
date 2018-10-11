# -*- coding: utf-8 -*-

def write(data, filename, mode='a'):
    """
    Escribe un archivo filename con los datos enviados en data
    
    @param data: datos a escribir
    @type data: string
    @param filename: nombre del archivo
    @type data: string
    @param mode: tipo de apertura del archivo
    @type data: string
    
    """
    f = open(filename, mode, encoding='utf8')
    f.write(data + '\n')
    f.close()

