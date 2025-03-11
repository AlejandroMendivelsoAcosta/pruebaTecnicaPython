from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear el objeto base para nuestras clases
Base = declarative_base()

# Definir la clase Empleado (tabla de la base de datos)
class Empleado(Base):
    __tablename__ = 'empleados'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String) 
    edad = Column(Integer)
    salario = Column(Integer)

    def __repr__(self):
        return f"<Empleado(id={self.id}, nombre={self.nombre}, edad={self.edad}, salario={self.salario})>"

# Crear la conexión a la base de datos
engine = create_engine('sqlite:///empresa.db')

# Crear la tabla en la base de datos (si no existe)
Base.metadata.create_all(engine)

# Crear la sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Función para insertar un empleado
def insertar_empleado(nombre, edad, salario):
    empleado = Empleado(nombre=nombre, edad=edad, salario=salario)
    session.add(empleado)
    session.commit()
    print("Empleado insertado correctamente")
    mostrar_empleados()

# Función para actualizar un empleado
def actualizar_empleado(id_empleado, nombre=None, edad=None, salario=None):
    empleado = session.query(Empleado).get(id_empleado)
    if empleado:
        if nombre:
            empleado.nombre = nombre
        if edad:
            empleado.edad = edad
        if salario:
            empleado.salario = salario
        session.commit()
        print("Empleado actualizado correctamente")
        mostrar_empleados()
    else:
        print("Empleado no encontrado")

# Función para eliminar un empleado
def eliminar_empleado(id_empleado):
    empleado = session.query(Empleado).get(id_empleado)
    if empleado:
        session.delete(empleado)
        session.commit()
        print("Empleado eliminado correctamente")
        mostrar_empleados()
    else:
        print("Empleado no encontrado")

# Función para obtener y mostrar todos los empleados
def mostrar_empleados():
    empleados = session.query(Empleado).all()
    print("\nLista de Empleados:")
    for emp in empleados:
        print(emp)

# Ejemplo de operaciones CRUD

# Insertar algunos empleados
insertar_empleado("Juan Pérez", 28, 35000)
insertar_empleado("Ana Gómez", 32, 40000)

# Actualizar un empleado
actualizar_empleado(1, edad=29, salario=37000)

# Eliminar un empleado
eliminar_empleado(2)

