import string

def conteoPalabras(conteo):

    conteo = conteo.lower()
    conteo = conteo.translate(str.maketrans("","", string.punctuation))
    palabras = conteo.split()

    conteo_palabras = {}

    for palabra in palabras:
        if palabra in conteo_palabras:
            conteo_palabras [palabra] += 1
        else:
            conteo_palabras [palabra] = 1

    return conteo_palabras  

conteo = input("Ingrese la frase: ")
conteo_palabras = conteoPalabras(conteo)
print("El conteo de las palabras son: ",conteo_palabras)