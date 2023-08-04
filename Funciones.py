from clases import Paciente

def nuevoPaciente(nombre, edad, raza):
    paciente_nuevo = Paciente(nombre,edad,raza)
    return paciente_nuevo
    
def quitarPaciente(self, paciente):
    
    if paciente in self.listado:
        self.listado.remove(paciente)
        print("Paciente eliminado exitosamente.")
    else:
        print("El paciente no está en la lista.")
                 
def listarPacientes(self):
    
    if not self.listado:
        print("No hay pacientes en la base de datos.")
    else:
        print("Listado de pacientes:")
        for i, paciente in enumerate(self.listado, 1):
            print(f"{i}. {paciente}")


def nuevaConsulta(self, motivo):
    if not self.listado:
        print("No hay pacientes en la base de datos.")
        return
    
        print("Lista de pacientes:")
        self.listarPacientes()
        opcion = int(input("Ingrese el número del paciente al que desea agregar una consulta: "))
        
        if 1 <= opcion <= len(self.listado):
            paciente_elegido = self.listado[opcion - 1]
            paciente_elegido.setConsulta(motivo)
            print("Consulta cargada exitosamente.")
        else:
            print("Opción inválida.")

def obtenerDetallePaciente(self, paciente):
        return paciente.getDatos()
