from tkinter import messagebox

class Persona:
    def __init__(self, nombre, edad, cui, telefono):
        self.__nombre = nombre
        self.__edad = edad
        self.__cui = cui
        self.__telefono = telefono
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @property
    def cui(self):
        return self.__cui
    @property
    def telefono(self):
        return self.__telefono
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @edad.setter
    def edad(self, edad):
        if edad.isdigit():
            if edad >= 0 and edad <=120:
                self.__edad = edad
            else:
                messagebox.showwarning("Error al ingresar edad", "Asegurese de ingresar una edad válida.")
        else:
            messagebox.showwarning("Error al ingresar edad", "Asegurese de que la edad sea un número entero.")

class Paciente(Persona):
    def __init__(self, nombre, edad, cui, telefono, motivo, tipo):
        super().__init__(nombre, edad, cui, telefono)
        self.__motivo = motivo
        self.__tipo = tipo

listadoPacientes = []
def registrarPaciente(cui, nombre, edad, telefono, motivo, tipo):
    p = Paciente(nombre, edad, cui, telefono, motivo, tipo)
    confirmar = messagebox.askokcancel("Registro de paciente", "Asegurese de que la información es correcta.\n¿Desea registrar al paciente?")
    if confirmar:
        listadoPacientes.append(p)
        messagebox.showinfo("Paciente registrado","El paciente ha sido registrado correctamente.")
        return True
    return False
def validacionesDatosNumericos(cui, edad, telefono):
    if edad.isdigit():
        if int(edad) >= 0 and int(edad) <= 120:
            if cui.isdigit():
                if len(cui) == 13:
                    if telefono.isdigit():
                        if len(telefono) == 8:
                            return True
                        else:
                            messagebox.showwarning("Error al ingresar teléfono", "Asegurese de que el teléfono tenga 8 dígitos.")
                    else:
                        messagebox.showwarning("Error al ingresar teléfono", "Asegurese de que el teléfono sea un número entero.")
                else:
                    messagebox.showwarning("Error al ingresar CUI", "Asegurese de que el CUI tenga 13 dígitos.")
            else:
                messagebox.showwarning("Error al ingresar CUI", "Asegurese de que el CUI sea un número entero.")
        else:
            messagebox.showwarning("Error al ingresar edad", "Asegurese de ingresar una edad válida.")
    else:
        messagebox.showwarning("Error al ingresar edad", "Asegurese de que la edad sea un número entero.")
    return False