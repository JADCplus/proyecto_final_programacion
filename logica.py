from tkinter import messagebox
import json

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
            if 0 <= edad <= 120:
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

class Usuario(Persona):
    def __init__(self, nombre, edad, cui, telefono, usuario, contra, tipo):
        super().__init__(nombre, edad, cui, telefono)
        self.__usuario = usuario
        self.__contra = contra
        self.__tipo = tipo

class Turno:
    def __init__(self, codigo, cui, nombre,estado):
        self.__codigo = codigo
        self.__cui = cui
        self.__nombre = nombre
        self.__estado = estado
    @property
    def codigo(self):
        return self.__codigo
    @property
    def cui(self):
        return self.__cui
    @property
    def nombre(self):
        return self.__nombre
    @property
    def estado(self):
        return self.__estado

def guardarPacientesGeneral(lista_objetos, nombre_archivo="pacientesGeneral.json"):
    datos_preparados = [p.__dict__ for p in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as info:
        json.dump(datos_preparados, info, indent=4, ensure_ascii=False)

def guardarTurnos(lista_objetos, nombre_archivo="infoTurnos.json"):
    datos_preparados = [p.__dict__ for p in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as info:
        json.dump(datos_preparados, info, indent=4, ensure_ascii=False)

def cargarPacientes(nombre_archivo="pacientesGeneral.json"):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        listaCargada = json.load(f)
    datosCargados=[]
    for lis in listaCargada:
        nombre = lis.pop("_Persona__nombre")
        edad = lis.pop("_Persona__edad")
        cui = lis.pop("_Persona__cui")
        telefono = lis.pop("_Persona__telefono")
        motivo = lis.pop("_Paciente__motivo")
        tipo = lis.pop("_Paciente__tipo")
        paci = Paciente(nombre,edad,cui,telefono,motivo,tipo)
        datosCargados.append(paci)
    return datosCargados

def pacientesTotales():
    return len(pacientesNormales)+len(pacientesUrgentes)
def pacientesParaConsulta():
    return len(pacientesNormales)
def pacientesParaUrgencia():
    return len(pacientesUrgentes)

def cargarTurnos(nombre_archivo = "infoTurnos.json"):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        listaCargada = json.load(f)
    datosCargados=[]
    for lis in listaCargada:
        codigo = lis.pop("_Turno__codigo")
        cui = lis.pop("_Turno__cui")
        nombre = lis.pop("_Turno__nombre")
        estado = lis.pop("_Turno__estado")
        turn = Turno(codigo,cui,nombre,estado)
        datosCargados.append(turn)
    return datosCargados

pacientesNormales = []
pacientesUrgentes = []
listadoPacientes = []
turnosGenerales = []
try:
    listadoPacientes = cargarPacientes()
    turnosGenerales = cargarTurnos()
    for tur in turnosGenerales:
        if tur.codigo[0]=="N":
            pacientesNormales.append(tur)
        else:
            pacientesUrgentes.append(tur)
except:
    pass
turnoNormales = len(pacientesNormales)+1
turnoUrgentes = len(pacientesUrgentes)+1
def registrarPaciente(cui, nombre, edad, telefono, motivo, tipo):
    global turnoNormales, turnoUrgentes

    p = Paciente(nombre, edad, cui, telefono, motivo, tipo)
    confirmar = messagebox.askokcancel("Registro de paciente", "Asegurese de que la información es correcta.\n¿Desea registrar al paciente?")
    if confirmar:
        if tipo == "Normal":
            codigo = "NOR"+str(turnoNormales)
            turnoNormales+=1
        else:
            codigo = "URG"+str(turnoUrgentes)
            turnoUrgentes+=1
        tur = Turno(codigo,cui,nombre,"En espera")
        turnosGenerales.append(tur)
        if tipo == "Normal":
            pacientesNormales.append(tur)
        else:
            pacientesUrgentes.append(tur)
        listadoPacientes.append(p)
        guardarTurnos(pacientesUrgentes+pacientesNormales)
        guardarPacientesGeneral(listadoPacientes)
        messagebox.showinfo(f"Paciente registrado","El paciente ha sido registrado correctamente."
                                                  f"\nEl código de turno del paciente es: {codigo}")
        return True
    return False

listadoUsuarios = []
def registrarUsuario(cui, nombre, edad, telefono, usuario, contra, tipo):
    u = Usuario(nombre,edad,cui,telefono,usuario,contra,tipo)
    confirmar = messagebox.askokcancel("Registro de usuario","Asegurese de que la información es correcta.\n¿Desea registrar el usuario?")
    if confirmar:
        listadoUsuarios.append(u)
        messagebox.showinfo("Usuario registrado", "El usuario ha sido registrado correctamente.")
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

def buscarPaciente(tipoBusqueda, datoIngresado):
    if not listadoPacientes:
        messagebox.showerror("Error al buscar paciente", "Aún no se ha ingresado ningún paciente.")
        return "No se ha ingresado ningún paciente"
    elif not datoIngresado:
        messagebox.showerror("Error al buscar paciente", "No se ingresó un dato para buscar.")
        return "Ingrese un dato para buscar."
    else:
        if tipoBusqueda == "CÓDIGO DE TURNO":
            for turno in turnosGenerales:
                if datoIngresado == turno.codigo:
                    for paciente in listadoPacientes:
                        if turno.cui == paciente.cui:
                            encontrado = paciente
                            return f"CUI: {encontrado.cui}\nNombre: {encontrado.nombre}\nEdad: {encontrado.edad}\nTeléfono: {encontrado.telefono}\nEstado: {turno.estado}"
        else:
            for paciente in listadoPacientes:
                if datoIngresado == paciente.cui:
                    for turno in turnosGenerales:
                        if turno.cui == datoIngresado:
                            encontrado = paciente
                            return f"CUI: {encontrado.cui}\nNombre: {encontrado.nombre}\nEdad: {encontrado.edad}\nTeléfono: {encontrado.telefono}\nEstado: {turno.estado}"
        return "Paciente no encontrado"