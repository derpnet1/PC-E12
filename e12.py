#Daniel Ernesto Rangel Perez
#Esteban Osorio Rodriguez

import argparse
from detectarEspañol import isSpanish

def cifrado(x,y) : 
    message = y
    espacios = 1
    while espacios > 0:
        clave = x
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    print(translated)

def descifrado(x,y) :
    message = y
    espacios = 1
    while espacios > 0:
        clave = x
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    key = len(clave)

    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?.'

    translated = ''

    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    print(translated)

def crackeo(x) :
    message = x
    SYMBOLS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz1234567890 !?.'

    # Loop through every possible key:
    for key in range(len(SYMBOLS)):
        # It is important to set translated to the blank string so that the
        # previous iteration's value for translated is cleared.
        translated = ''

        # The rest of the program is almost the same as the original program:

        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                # Handle the wrap-around:
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]

            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        # Display every possible decryption:
        #isEnglish(translated)
        #print('Key #%s: %s' % (key, translated))

        if isSpanish(translated) :
           print('Key #%s: %s' % (key, translated))

#Argparse
description = """Script para cifrar, descifrar y crackear por Cesar

            Ejemplos de uso:

                + python e12.py -c clave cifrado
                + py e12.py -d clave krñd
                + python e12.py -cr krñd
            Aclaraciones de uso:
                +En caso de enviar mensaje solo en cifrado con 2 o mas palabras
                 usar comillas
                 Ejemplo de 2 o mas palabras:
                  +python e12.py -c clave "hola mundo"
                + En caso de usar crackeo no se utiliza clave
                + En clave podemos usar cualquier palabra """
                
            

parser = argparse.ArgumentParser(description='Cifrado, descifrado y crackeo con Cesar',

                                 epilog=description,

                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-c", nargs=2, metavar=('clave', 'mensaje'), 
                    dest="cifrado",help="Algo para cifrar")

parser.add_argument("-d", nargs=2, metavar=('clave', 'mensaje'), dest='descifrado',
                     help="Algo para descifrar")

parser.add_argument("-cr", metavar='-crackeo', dest='crackeo', help="Algo para crackear")
#parser.add_argument('clave', metavar='clave', help='Clave cifrar o descifrar', default="default")
params = parser.parse_args()

x = (params.cifrado)
b = (params.descifrado)
a = (params.crackeo)


if x != None:
    cifrado(x[0], x[1])
elif b != None:
    descifrado(b[0], b[1])
elif a != None:
    crackeo(a)
