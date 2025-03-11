empleados = [
{"nombre": "Carlos", "edad": 35, "salario": 55000},
 {"nombre": "Ana", "edad": 28, "salario": 48000},
 {"nombre": "Luis", "edad": 40, "salario": 62000},
 {"nombre": "Sofía", "edad": 32, "salario": 70000},
 {"nombre": "Pedro", "edad": 45, "salario": 52000}
 ]

def infoEmpleado(empleados):

    #Fitro de nombre de empleados por ganacia
    ganaciaMayor = []
    for empleado in empleados: 
        if empleado['salario'] > 50000:
            ganaciaMayor.append(empleado['nombre'])
    # Promedio de la lista 
    salarios = [empleado['salario'] for empleado in empleados]
    promedioSalario = sum(salarios)/len(salarios)

    return ganaciaMayor, promedioSalario

ganaciaMayor, promedioSalario = infoEmpleado(empleados)

print("Esto es una prueba",ganaciaMayor )
print(" promedio Salario: ", promedioSalario)