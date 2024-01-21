"""
Chatbot analizador de sentimientos

En este proyecto, podrias desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y no responda cual es el sentimiento.

Este proyecto te daria la oportunidad de trabajar con varios aspectos de la Programacion Orientada a Objetos, modulos, API, analisis de datos, etc.
"""

import os

from googletrans import Translator
from textblob import TextBlob

global ENGLISH, ESPAÑOL
ENGLISH: str = "en"
ESPAÑOL: str = "es"


def borrar() -> None:
    os.system(command="cls" if os.name == "nt" else "clear")


# ! en-English
# !  es-Spanish


class Español:
    def __init__(self: object) -> None:
        self._traductor_español: object = Translator()

    def _Traducir_Texto_Español(self: object, texto: str) -> str:
        texto_español: any = self._traductor_español.translate(
            text=texto, dest=ESPAÑOL, src=ENGLISH
        )
        return texto_español.text


class Ingles:
    def __init__(self: object) -> None:
        self._traductor_ingles: object = Translator()

    """
    >>> La funcion traducir texto recibe un texto y lo traduce a otro idioma
    >>> El parametro texto que es de tipo str es el texto que se va a traducir
    """
    # Retorna el idioma de la palabra que se le pasa por parametro

    def _Traducir_Texto_Ingles(self: object, texto: str, idioma_detectado: str) -> str:
        """
        la biblioteca googletrans y su método translate, text, dest y src son argumentos que especifican detalles sobre cómo se debe realizar la traducción:

        text: Este es el texto que quieres traducir. Debe ser una cadena de texto.

        dest: Este es el idioma al que quieres traducir el texto. Debe ser una cadena de texto que represente el código de idioma de destino (por ejemplo, 'en' para inglés, 'es' para español, etc.).

        src: Este es el idioma del texto original. Debe ser una cadena de texto que represente el código de idioma de origen (por ejemplo, 'en' para inglés, 'es' para español, etc.). Si no se especifica, googletrans intentará detectar automáticamente el idioma.
        """

        # Si la palabra no esta en ingles la traduce a ingles
        try:
            if idioma_detectado != ENGLISH:
                self._texto_traducido: any = self._traductor_ingles.translate(
                    text=texto, dest=ENGLISH, src=idioma_detectado
                )

                return self._texto_traducido.text

            # En este caso la palabra esta en ingles
            else:
                return texto

        except TypeError:
            return (
                "Error al detectar el idioma de la palabra ingrese minimo 7 caracteres"
            )


class Traductor(Ingles, Español):
    def __init__(self: object) -> None:
        Ingles.__init__(self=self)
        Español.__init__(self=self)
        self._traductor: object = Translator()

    def _Ver_Idioma(
        self: object,
        palabra: str,
    ) -> str:
        idioma: str = self._traductor.detect(
            text=palabra,
        ).lang

        return super()._Traducir_Texto_Ingles(texto=palabra, idioma_detectado=idioma)


class AnalizadorSentimientos(Traductor):
    def __init__(self: object) -> None:
        super().__init__()

    def _Analizador_Sentimientos(self: object, texto: str) -> str:
        texto_traducido: str = super()._Ver_Idioma(palabra=texto)

        analisis: object = TextBlob(text=texto_traducido)
        if analisis.sentiment.polarity > 0:
            return f"""
{super()._Traducir_Texto_Español(texto=texto_traducido)} 
\033[32m"El comentario que hiciste indica que tu estado de animo es positivo"
"""
        elif analisis.sentiment.polarity == 0:
            return f"""
{super()._Traducir_Texto_Español(texto=texto_traducido)} 
\033[33m"El comentario que hiciste indica que tu estado de animo es neutral"
"""
        else:
            return f"""
{super()._Traducir_Texto_Español(texto=texto_traducido)} 
\033[31m"El comentario que hiciste indica que te sientes mal"
"""


"""
# Códigos de colores ANSI. EL formato de texto van del 0 al 9, y los códigos para los colores del texto y del fondo van del 30 al 47.

\033[0m: Reset (restablece todos los atributos de formato)
\033[1m: Bright (aumenta la intensidad del color)
\033[2m: Dim (disminuye la intensidad del color)
\033[3m: Italic (texto en cursiva)
\033[4m: Underlined (texto subrayado)
\033[7m: Reverse (invierte los colores de fondo y de texto)
\033[8m: Hidden (texto oculto)


Para cambiar el color del texto:

\033[30m: Black (negro)
\033[31m: Red (rojo)
\033[32m: Green (verde)
\033[33m: Yellow (amarillo)
\033[34m: Blue (azul)
\033[35m: Magenta (magenta)
\033[36m: Cyan (cian)
\033[37m: White (blanco)
Para cambiar el color de fondo:

\033[40m: Black (negro)
\033[41m: Red (rojo)
\033[42m: Green (verde)
\033[43m: Yellow (amarillo)
\033[44m: Blue (azul)
\033[45m: Magenta (magenta)
\033[46m: Cyan (cian)
\033[47m: White (blanco)
"""

if __name__ == "__main__":
    daniel = AnalizadorSentimientos()

    while True:
        borrar()

        texto_usuario: str = str(
            input("\033[36mIngrese un texto de tu estado de animo: ")
        ).lower()
        print("\033[0m")
        try:
            print(daniel._Analizador_Sentimientos(texto=texto_usuario))
        except (TypeError, ValueError):
            # * usar paréntesis para capturar múltiples excepciones.
            print(
                "Error al detectar el idioma de la palabra ingrese minimo 7 caracteres"
            )

        print("\033[0m")

        while True:
            texto_usuario: str = str(
                input("Quires seguir con el programa (Si/No): ")
            ).lower()
            if texto_usuario == "no":
                exit(code="Fin del programa")
            elif texto_usuario == "si":
                break
            else:
                print("\033[0m")

# Linux o Mac
# si no tenemos instalado pip sudo apt-get install python3-pip
# pip3 install textblob
# python3 -m pip install textblob

# Windows
# pip install textblob
# py -m pip install textblob


"""
    Todos los idiomas 
    lang
    en-English
    es-Spanish
    fr-French
    de-German
    it-Italian
    pt-Portuguese
    af-Afrikaans
    sq-Albanian
    am-Amharic
    ar-Arabic
    hy-Armenian
    az-Azerbaijani
    eu-Basque
    be-Belarusian
    bn-Bengali
    bs-Bosnian
    bg-Bulgarian
    ca-Catalan
    ceb-Cebuano
    ny-Chichewa
    zh-CN - Chinese (Simplified)
    zh-TW - Chinese (Traditional)
    co - Corsican
    hr - Croatian
    cs - Czech
    da - Danish
    nl - Dutch
    eo - Esperanto
    et - Estonian
    tl - Filipino
    fi - Finnish
    fy - Frisian
    gl - Galician
    ka - Georgian
    el - Greek
    gu - Gujarati
    ht - Haitian Creole
    ha - Hausa
    haw - Hawaiian
    iw - Hebrew
    hi - Hindi
    hmn - Hmong
    hu - Hungarian
    is - Icelandic
    ig - Igbo
    id - Indonesian
    ga - Irish
    ja - Japanese
    jw - Javanese
    kn - Kannada
    kk - Kazakh
    km - Khmer
    ko - Korean
    ku - Kurdish (Kurmanji)
    ky - Kyrgyz
    lo - Lao
    la - Latin
    lv - Latvian
    lt - Lithuanian
    lb - Luxembourgish
    mk - Macedonian
    mg - Malagasy
    ms - Malay
    ml - Malayalam
    mt - Maltese
    mi - Maori
    mr - Marathi
    mn - Mongolian
    my - Burmese
    ne - Nepali
    no - Norwegian
    ps - Pashto
    fa - Persian
    pl - Polish
    pa - Punjabi
    ro - Romanian
    ru - Russian
    sm - Samoan
    gd - Scots Gaelic
    sr - Serbian
    st - Sesotho
    sn - Shona
    sd - Sindhi
    si - Sinhala
    sk - Slovak
    sl - Slovenian
    so - Somali
    es - Spanish
    su - Sundanese
    sw - Swahili
    sv - Swedish
    tg - Tajik
    ta - Tamil
    te - Telugu
    th - Thai
    tr - Turkish
    uk - Ukrainian
    ur - Urdu
    uz - Uzbek
    vi - Vietnamese
    cy - Welsh
    xh - Xhosa
    yi - Yiddish
    yo - Yoruba
    zu - Zulu
    
"""
