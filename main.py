from clases import Veterinaria,Paciente
from Funciones import nuevoPaciente, quitarPaciente, listarPacientes, nuevaConsulta, obtenerDetallePaciente
    
def mostrar_bienvenida():
    print("Bienvenido a la Veterinaria!")
    print("----------------------------")

def progPrincipal():
    mostrar_bienvenida()

def listar_pacientes(veterinaria):
    pacientes = veterinaria.getListado()
    if not pacientes:
        print("No hay pacientes en la base de datos.")
    else:
        print("Listado de pacientes:")
        for i, paciente in enumerate(pacientes, 1):
            print(f"{i}. {paciente}")

def detallar_paciente(veterinaria):
    listar_pacientes(veterinaria)
    opcion = int(input("Ingrese el número del paciente que desea detallar: "))
    pacientes = veterinaria.getListado()
    if 1 <= opcion <= len(pacientes):
        paciente_elegido = pacientes[opcion - 1]
        print("Detalles del paciente:")
        
        print(paciente_elegido)
    else:
        print("Opción inválida.")

def cargar_nuevo_paciente(veterinaria):
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    raza = input("Ingrese la raza del paciente: ")
    paciente_nuevo = nuevoPaciente(nombre,edad,raza)
    veterinaria.setPaciente(paciente_nuevo)
    print("Paciente cargado exitosamente.")

def quitar_paciente(veterinaria):
    listar_pacientes(veterinaria)
    opcion = int(input("Ingrese el número del paciente que desea quitar: "))
    pacientes = veterinaria.getListado()
    if 1 <= opcion <= len(pacientes):
        paciente_quitar = pacientes[opcion - 1]
        veterinaria.deletePaciente(paciente_quitar)
        print("Paciente eliminado exitosamente.")
    else:
        print("Opción inválida.")

def cargar_consulta(veterinaria):
    listar_pacientes(veterinaria)
    opcion = int(input("Ingrese el número del paciente para agregar una consulta: "))
    pacientes = veterinaria.getListado()
    if 1 <= opcion <= len(pacientes):
        paciente_elegido = pacientes[opcion - 1]
        motivo = input("Ingrese el motivo de la consulta: ")
        paciente_elegido.setConsulta(motivo)

        print("Consulta cargada exitosamente.")
    else:
        print("Opción inválida.")
    
def dar_alta_tratamiento(veterinaria):
    listar_pacientes(veterinaria)
    opcion = int(input("Ingrese el número del paciente al que desea dar de alta el tratamiento médico: "))
    pacientes = veterinaria.getListado()
    if 1 <= opcion <= len(pacientes):
        paciente_elegido = pacientes[opcion - 1]
        paciente_elegido.paciente_con_tratamiento = True
        print("Tratamiento médico dado de alta.")
    else:
        print("Opción inválida.")

def despedida():
    print("¡Hasta luego! Gracias por utilizar nuestro sistema.")

def progPrincipal():
    veterinaria = Veterinaria()
    mostrar_bienvenida()

    while True:
        print("\nOpciones:")
        print("1. Lista de  pacientes")
        print("2. Detalles de paciente")
        print("3. Cargar nuevo paciente")
        print("4. Quitar paciente")
        print("5. Cargar consulta")
        print("6. Dar alta tratamiento médico")
        print("7. Salir")

        opcion = int(input("Ingrese el número de la opción que desea realizar: "))

        if opcion == 1:
            listar_pacientes(veterinaria)
        elif opcion == 2:
            detallar_paciente(veterinaria)
        elif opcion == 3:
            cargar_nuevo_paciente(veterinaria)
        elif opcion == 4:
            quitar_paciente(veterinaria)
        elif opcion == 5:
            cargar_consulta(veterinaria)
        elif opcion == 6:
            dar_alta_tratamiento(veterinaria)
        elif opcion == 7:
            despedida()
            break
        else:
            print("Opción inválida. Por favor, elija una opción válida nuevamente.")
progPrincipal()