import concurrent.futures

def calcularCuadrado(num):
    return num ** 2

def calculo(numeros):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = list(executor.map(calcularCuadrado, numeros))
    return result

if __name__ == "__main__": 
    numeros = [1, 2, 3, 4, 5]
    result = calculo(numeros)
    print(result)
