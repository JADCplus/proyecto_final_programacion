from tkinter import messagebox
from collections import deque
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
        self.__edad = edad
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

class Paciente(Persona):
    def __init__(self, nombre, edad, cui, telefono, motivo, tipo):
        super().__init__(nombre, edad, cui, telefono)
        self.__motivo = motivo
        self.__tipo = tipo
    @property
    def tipo(self):
        return self.__tipo
    @property
    def motivo(self):
        return self.__motivo
    @motivo.setter
    def motivo(self, motivo):
        self.__motivo = motivo

class Usuario(Persona):
    def __init__(self, nombre, edad, cui, telefono, user, contra, tipo):
        super().__init__(nombre, edad, cui, telefono)
        self.__user = user
        self.__contra = contra
        self.__tipo = tipo
    @property
    def user(self):
        return self.__user
    @property
    def contra(self):
        return self.__contra
    @property
    def tipo(self):
        return self.__tipo
    @user.setter
    def user(self,user):
        self.__user = user
    @contra.setter
    def contra(self,contra):
        self.__contra = contra
    @tipo.setter
    def tipo(self,tipo):
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
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @estado.setter
    def estado(self, estado):
        self.__estado = estado

def guardarPacientesGeneral(lista_objetos, nombre_archivo="pacientesGeneral.json"):
    datos_preparados = [p.__dict__ for p in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as info:
        json.dump(datos_preparados, info, indent=4, ensure_ascii=False)

def guardarTurnos(lista_objetos, nombre_archivo="infoTurnos.json"):
    datos_preparados = [p.__dict__ for p in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as info:
        json.dump(datos_preparados, info, indent=4, ensure_ascii=False)

def guardarHistorialTurnos(lista_objetos, nombre_archivo="historialTurnos.json"):
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

def pacientesEnTotal():
    return len(listadoPacientes)
def pacientesEnEspera():
    return len(pacientesNormales)+len(pacientesUrgentes)
def pacientesTotalesAtendidos():
    contador = 0
    for pac in historialTurnos:
        if pac.estado == "Atendido":
            contador += 1
    return contador
def pacientesTotalesCancelados():
    contador = 0
    for pac in historialTurnos:
        if pac.estado == "Cancelado":
            contador += 1
    return contador

def pacientesParaConsulta():
    return len(pacientesNormales)
def atenderConsulta():
    for paciente in listadoPacientes:
        if paciente.cui == pacientesNormales[0].cui:
            return paciente

def pacientesParaUrgencia():
    return len(pacientesUrgentes)
def atenderUrgencia():
    for paciente in listadoPacientes:
        if paciente.cui == pacientesUrgentes[0].cui:
            return paciente

def finalizarAtencion(tipo):
    confirmacion = messagebox.askyesno("Confirmación de finalización", "¿Desea finalizar la atención del paciente?")
    if confirmacion:
        if tipo == "Normal":
            atendido = pacientesNormales.popleft()
        else:
            atendido = pacientesUrgentes.popleft()
        for turno in historialTurnos:
            if atendido.codigo == turno.codigo:
                turno.estado = "Atendido"
                break
        guardarTurnos(pacientesUrgentes + pacientesNormales)
        guardarHistorialTurnos(historialTurnos)
        agregarAccion(f"Se atendió el turno de código {atendido.codigo}", atendido)
        messagebox.showinfo("Atención finalizada", "Se ha atentido al paciente.")

def cancelarAtencion(tipo):
    confirmacion = messagebox.askyesno("Confirmación de cancelación", "¿Desea cancelar la atención del paciente?")
    if confirmacion:
        if tipo == "Normal":
            atendido = pacientesNormales.popleft()
        else:
            atendido = pacientesUrgentes.popleft()
        for turno in historialTurnos:
            if atendido.codigo == turno.codigo:
                turno.estado = "Cancelado"
                break
        guardarHistorialTurnos(historialTurnos)
        guardarTurnos(pacientesUrgentes + pacientesNormales)
        agregarAccion(f"Se canceló el turno de código {atendido.codigo}",atendido)
        messagebox.showinfo("Atención cancelada", "Se ha cancelado la atención al paciente.")

def cargarTurnos(nombre_archivo = "historialTurnos.json"):
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

pacientesNormales = deque()
pacientesUrgentes = deque()
listadoPacientes = []
turnosGenerales = []
historialTurnos = []
cantidadNormales=0
cantidadUrgentes=0
try:
    listadoPacientes = cargarPacientes()
    turnosGenerales = cargarTurnos(nombre_archivo = "infoTurnos.json")
    historialTurnos = cargarTurnos()
    for tur in historialTurnos:
        if tur.codigo[0]=="N" and tur.estado == "En espera":
            pacientesNormales.append(tur)
            cantidadNormales += 1
        elif tur.codigo[0]=="U" and tur.estado == "En espera":
            pacientesUrgentes.append(tur)
            cantidadUrgentes += 1
        if tur.codigo[0]=="N": cantidadNormales += 1
        else: cantidadUrgentes += 1
except:
    pass

def registrarPaciente(cui, nombre, edad, telefono, motivo, tipo):
    global cantidadNormales, cantidadUrgentes
    cuiExistente = False
    if len(listadoPacientes)>0:
        for paciente in listadoPacientes:
            if cui == paciente.cui:
                cuiExistente = True
                messagebox.showerror("Error al ingresar paciente.","Ya hay un paciente registrado con ese número de CUI.")
                break
    if not cuiExistente:
        p = Paciente(nombre, edad, cui, telefono, motivo, tipo)
        confirmar = messagebox.askokcancel("Registro de paciente",
                                           "Asegurese de que la información es correcta.\n¿Desea registrar al paciente?")
        if confirmar:
            if tipo == "Normal":
                codigo = "NOR" + str(cantidadNormales)
                cantidadNormales += 1
            else:
                codigo = "URG" + str(cantidadUrgentes)
                cantidadUrgentes += 1
            tur = Turno(codigo, cui, nombre, "En espera")
            turnosGenerales.append(tur)
            if tipo == "Normal":
                pacientesNormales.append(tur)
            else:
                pacientesUrgentes.append(tur)
            listadoPacientes.append(p)
            historialTurnos.append(tur)
            guardarHistorialTurnos(historialTurnos)
            guardarTurnos(pacientesUrgentes + pacientesNormales)
            guardarPacientesGeneral(listadoPacientes)
            agregarAccion(f"Se registró al paciente con código de turno {tur.codigo}",tur)
            messagebox.showinfo(f"Paciente registrado", "El paciente ha sido registrado correctamente."
                                                        f"\nEl código de turno del paciente es: {codigo}")
            return True
        return False

#Métodos relacionados a usuarios
listadoUsuarios = []
def guardarUsuarios(lista_objetos, nombre_archivo="usuarios.json"):
    datos_preparados = [p.__dict__ for p in lista_objetos]
    with open(nombre_archivo, "w", encoding="utf-8") as info:
        json.dump(datos_preparados, info, indent=4, ensure_ascii=False)
def cargarUsuarios(nombre_archivo="usuarios.json"):
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        listaCargada = json.load(f)
    datosCargados=[]
    for lis in listaCargada:
        nombre = lis.pop("_Persona__nombre")
        edad = lis.pop("_Persona__edad")
        cui = lis.pop("_Persona__cui")
        telefono = lis.pop("_Persona__telefono")
        usuario = lis.pop("_Usuario__user")
        contra = lis.pop("_Usuario__contra")
        tipo = lis.pop("_Usuario__tipo")
        usua = Usuario(nombre,edad,cui,telefono,usuario,contra,tipo)
        datosCargados.append(usua)
    return datosCargados
try:
    listadoUsuarios = cargarUsuarios()
except:
    pass
def registrarUsuario(cui, nombre, edad, telefono, usuario, contra, tipo):
    u = Usuario(nombre,edad,cui,telefono,usuario,contra,tipo)
    if not validarDatosRepetidos(cui,usuario,"registrar"):
        confirmar = messagebox.askokcancel("Registro de usuario","Asegurese de que la información es correcta.\n¿Desea registrar el usuario?")
        if confirmar:
            listadoUsuarios.append(u)
            agregarAccion(f"Se registró el usuario {u.user}",u)
            messagebox.showinfo("Usuario registrado", "El usuario ha sido registrado correctamente.")
            guardarUsuarios(listadoUsuarios)
            return True
    return False
def validarDatosRepetidos(cui,usuario, accion):
    existente = False
    for usu in listadoUsuarios:
        if usu.cui == cui and accion == "registrar":
            existente = True
            messagebox.showwarning("Error al registrar usuario", "Ya hay un usuario con ese número de CUI.")
            break
        elif usu.user == usuario:
            existente = True
            if accion == "registrar":
                messagebox.showwarning("Error al registrar usuario", "Ese nombre de usuario ya está en uso.")
            else:
                messagebox.showwarning("Error al modificar usuario", "Ese nombre de usuario ya está en uso.")
            break
    return existente

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
            for turno in historialTurnos:
                if datoIngresado == turno.codigo:
                    for paciente in listadoPacientes:
                        if turno.cui == paciente.cui:
                            encontrado = paciente
                            return f"CUI: {encontrado.cui}\nNombre: {encontrado.nombre}\nEdad: {encontrado.edad}\nTeléfono: {encontrado.telefono}\nEstado: {turno.estado}"
        else:
            for paciente in listadoPacientes:
                if datoIngresado == paciente.cui:
                    for turno in historialTurnos:
                        if turno.cui == datoIngresado:
                            encontrado = paciente
                            return f"CUI: {encontrado.cui}\nNombre: {encontrado.nombre}\nEdad: {encontrado.edad}\nTeléfono: {encontrado.telefono}\nEstado: {turno.estado}"
        return "Paciente no encontrado"

#Métodos de modificación de datos
def usuarioParaModificar(cui):
    for usu in listadoUsuarios:
        if usu.cui == cui:
            return usu
    messagebox.showwarning("Usuario no encontrado", "No se encontró ningún usuario con ese\nnúmero de CUI.")
    return None
def modificarDatosUsuario(cui,nombre,edad,telefono,user,contra):
    encontrado = False
    for u in listadoUsuarios:
        if u.cui == cui:
            guardar = u
            u.nombre=nombre
            u.edad=edad
            u.telefono=telefono
            u.contra=contra
            u.user=user
            encontrado = True
            agregarAccion(f"Se modificaron los datos del usuario {guardar.user}",guardar)
            guardarUsuarios(listadoUsuarios)
            break
    if not encontrado:
        messagebox.showwarning("Error al modificar", "Asegurese de no modificar el número de CUI.")
    else:
        messagebox.showinfo("Información modificada", "La información del usuario se modificó correctamente.")


def pacienteParaModificar(cui):
    for paci in listadoPacientes:
        if paci.cui == cui:
            return paci
    messagebox.showwarning("Paciente no encontrado", "No se encontró ningún paciente con ese\nnúmero de CUI.")
    return None
def modificarInfoPaciente(cui,nombre,edad,telefono,motivo):
    encontrado = False
    for paci in listadoPacientes:
        if paci.cui == cui:
            paci.nombre=nombre
            paci.edad=edad
            paci.telefono=telefono
            paci.motivo=motivo
            guardarPacientesGeneral(listadoPacientes)
            encontrado = True
            break
    for turno in historialTurnos:
        if turno.cui == cui:
            turno.nombre=nombre
            guardarHistorialTurnos(historialTurnos)
            break
    for turno in pacientesNormales:
        if turno.cui == cui:
            turno.nombre=nombre
            break
    for turno in pacientesUrgentes:
        if turno.cui == cui:
            turno.nombre=nombre
            break
    guardarTurnos(pacientesUrgentes + pacientesNormales)
    if not encontrado:
        messagebox.showwarning("Error al modificar", "Asegurese de no modificar el número de CUI.")
    else:
        messagebox.showinfo("Información modificada", "La información del paciente se modificó correctamente.")

#Historial de acciones
historialAcciones=[]
def agregarAccion(mensaje, accion):
    historialAcciones.append(mensaje)

#login
def verificarLogin(usu,contra):
    for us in listadoUsuarios:
        if us.user == usu and us.contra == contra:
            messagebox.showinfo("Sesión iniciada", "Ha iniciado sesión correctamente.")
            return True
    messagebox.showerror("Error al iniciar sesión", "Usuario o contraseña incorrectos")
    return False
def tipoUsuario(usu,contra):
    for us in listadoUsuarios:
        if us.user == usu and us.contra == contra:
            return us