class Veterinaria:
    def __init__(self):
        self.listado = []

    def setPaciente(self, paciente):
        self.listado.append(paciente)

    def deletePaciente(self, paciente):
        for i in self.listado:
            if i == paciente:
                self.listado.remove(i)
                break

    def getListado(self):
        return self.listado

    def __str__(self):
        return f"Cantidad de pacientes en la veterinaria: {len(self.listado)}"
    
class Paciente:
    def __init__(self, nombre: str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} - {self.edad}"


# Crear una instancia de la clase Veterinaria
veterinaria = Veterinaria()

# Agregar pacientes a la veterinaria
veterinaria.setPaciente(Paciente("Procer", "4"))
veterinaria.setPaciente(Paciente("Marly", "3"))
veterinaria.setPaciente(Paciente("Nemo", "5"))

# Obtener el listado de pacientes
print("Listado de pacientes:")
for i in veterinaria.getListado():
    print(i)

# Eliminar un paciente
paciente_a_eliminar = Paciente("Marley", "3")
veterinaria.deletePaciente(paciente_a_eliminar)

# Obtener el listado de pacientes después de eliminar uno
print("\nListado de pacientes después de eliminar uno:")
for i in veterinaria.getListado():
    print(i)

# Obtener la cantidad de pacientes utilizando el método mágico __str__
def __str__(self):
    print(veterinaria)

class Animal:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Paciente(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
        self.consultas = []
        self.paciente_con_tratamiento = False

    def __str__(self):
        cant_consultas = len(self.consultas)
        return f"{super().__str__()}, Raza: {self.raza}, Consultas: {cant_consultas}, Paciente con tratamiento médico: {self.paciente_con_tratamiento}"
    
   
    
    def setConsulta(self, consulta):
        self.consultas.append(consulta)

    def getDatos(self):
        datos_paciente = [self.nombre, self.edad, self.raza, self.consultas, self.paciente_con_tratamiento]
        return datos_paciente