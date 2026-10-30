import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time

# Colores del proyecto
COLOR_PRINCIPAL = "#0097A7"
COLOR_OSCURO = "#00646E"
COLOR_CLARO = "#E0F7FA"
COLOR_BLANCO = "#FFFFFF"
COLOR_GRIS = "#696969"


# ventana login
def login():
    ventana_login = tk.Tk()
    ventana_login.title("Login")
    ventana_login.geometry('1300x770')
    ventana_login.resizable(False, False)
    ventana_login.config(bg=COLOR_BLANCO)
    icono_ventana_login = tk.PhotoImage(file="login.png")
    ventana_login.iconphoto(False, icono_ventana_login)

    canvas_fondo = tk.Canvas(ventana_login, width=650, height=800, bg=COLOR_PRINCIPAL)
    canvas_fondo.place(x=0, y=0)

    label_titulo_1 = tk.Label(ventana_login, text="CLI",
                              font=("Sans-Serif", 70, "bold"),
                              fg=COLOR_BLANCO,
                              bg="#0097A7")
    label_titulo_1.place(x=495, y=50)

    label_titulo_2 = tk.Label(ventana_login, text="NICA",
                              font=("Sans-Serif", 70, "bold"),
                              fg="#00646E",
                              bg="#FFFFFF")
    label_titulo_2.place(x=652, y=50)

    label_titulo_3 = tk.Label(ventana_login, text="LOGIN",
                              font=("Sans-Serif", 20, "bold"),
                              fg="#C4C4C4",
                              bg="#FFFFFF")
    label_titulo_3.place(x=790, y=140)

    canva_fondo_login = tk.Canvas(ventana_login, width=570, height=525, bg="#FFFFFF")
    canva_fondo_login.place(x=78, y=200)

    canva_fondo_login2 = tk.Canvas(ventana_login, width=570, height=525, bg="#E0F7FA")
    canva_fondo_login2.place(x=650, y=200)

    label_titulo_cuadro_login = tk.Label(ventana_login, text="CLINICA",
                                         font=("Sans-Serif", 25, "bold"),
                                         fg="#00646E",
                                         bg="#FFFFFF")
    label_titulo_cuadro_login.place(x=300, y=280)

    label_usuario = tk.Label(ventana_login, text="USUARIO",
                             font=("Sans-Serif", 10, "bold"),
                             fg="#696969",
                             bg="#FFFFFF"
                             )
    label_usuario.place(x=215, y=355)

    entry_usuario = tk.Entry(ventana_login, bg="#FFFFFF",
                             fg="black",
                             font=("Sans-Serif", 15, "bold"))
    entry_usuario.place(x=215, y=375, width=300, height=40)

    label_password = tk.Label(ventana_login, text="CONTRASEÑA",
                              font=("Sans-Serif", 10, "bold"),
                              fg="#696969",
                              bg="#FFFFFF"
                              )
    label_password.place(x=215, y=480)

    entry_password = tk.Entry(ventana_login, bg="#FFFFFF",
                              fg="black",
                              font=("Sans-Serif", 15, "bold"),
                              show="*",
                              )
    entry_password.place(x=215, y=500, width=300, height=40)

    boton_confirmar = tk.Button(ventana_login, text="INGRESAR",
                                font=("Sans-Serif", 10, "bold"),
                                fg="#FFFFFF",
                                bg="#0097A7")
    boton_confirmar.place(x=260, y=600, width=200, height=40)

    img = Image.open("clinica.png").resize((350, 350))
    imagen_clinica = ImageTk.PhotoImage(img)

    mostrar = tk.Label(ventana_login, image=imagen_clinica, bg="#E0F7FA")
    mostrar.image = imagen_clinica  # evita que se borre
    mostrar.place(x=770, y=280)

    entry_usuario.focus_set()
    ventana_login.mainloop()


def ventana_principal_admin():

    def mostrar_frame(frame):
        frame.tkraise()  # funcion para traer el frame al frente

    def label(padre,texto,pos_x, pos_y, color_texto, fondo_texto):
        tk.Label(padre,
                 text=texto,
                 font=("Sans-Serif", 10, "bold"),
                 fg=color_texto, bg=fondo_texto
                 ).place(x=pos_x , y=pos_y)

    def boton(padre,texto,pos_x, pos_y, color_texto, fondo_texto,relieve,ancho,alto, comando=None):
        tk.Button(padre,
                  text=texto,
                  font=("Sans-Serif", 8, "bold"),
                  fg=color_texto, bg=fondo_texto,
                  activebackground=COLOR_OSCURO, #color de fondo mientras se hace click
                  activeforeground=COLOR_BLANCO, #color de la letra mientras se hace click
                  relief=relieve, bd=0, cursor="hand2", #relief: estilo del borde , bd: grosor del borde
                  anchor="w", command=comando).place(x=pos_x, y=pos_y, width=ancho, height=alto)

    def tarjeta(padre,pos_x, pos_y,ancho, alto, titulo, tam_titulo, tam_numero, con_numero=True  ):
        cuadro = tk.Frame(padre,
                           width=ancho, height=alto,
                           bg=COLOR_CLARO,
                           highlightbackground=COLOR_OSCURO, #color del borde
                           highlightthickness=4) #grosor del borde

        cuadro.place(x=pos_x, y=pos_y, width=ancho, height=alto)

        tk.Label(cuadro, text=titulo,
                 font=("Sans-Serif", tam_titulo, "bold"),
                 fg=COLOR_OSCURO, bg=COLOR_CLARO,
                 justify="center").place(relx=0, rely=0.12, relwidth=1)

        if not con_numero:
            return cuadro, None

        numero = tk.Label(cuadro, text="0",
                          font=("Sans-Serif", tam_numero, "bold"),
                          fg=COLOR_PRINCIPAL, bg=COLOR_CLARO)
        numero.place(relx=0, rely=0.62, relwidth=1)
        return cuadro, numero

    def actualizar_estadisticas():

        label_fecha_hora.config(text=time.strftime("%d/%m/%Y\n%H:%M:%S"))
        ventana_principal_admin.after(1000, actualizar_estadisticas)  # se repite cada segundo

    ventana_principal_admin = tk.Tk()
    ventana_principal_admin.title("CLINICA MEDICA")
    ventana_principal_admin.geometry("1300x770")
    icono = tk.PhotoImage(file="clinica.png")
    ventana_principal_admin.iconphoto(False, icono)
    ventana_principal_admin.resizable(False, False)

    barra_lateral = tk.Canvas(ventana_principal_admin, width=250, height=764, bg="#0097A7",
                              highlightbackground=COLOR_OSCURO,
                              highlightthickness=3)
    barra_lateral.place(x=0, y=0)

    # GESTIONES PRINCIPALES

    label(barra_lateral,"GESTIONES", 30, 25, COLOR_BLANCO, COLOR_PRINCIPAL)
    boton(barra_lateral,"REGISTRAR PACIENTE",40, 70,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_registrar_paciente))
    boton(barra_lateral,"GENERAR TURNO",40, 120,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))
    boton(barra_lateral,"CANCELAR TURNO",40, 170,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))
    boton(barra_lateral,"BUSCAR PACIENTE", 40,220,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))

    # HISTORIAL

    label(barra_lateral,"HISTORIAL",30, 270, COLOR_BLANCO, COLOR_PRINCIPAL)
    boton(barra_lateral,"ACCIONES",40,320,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))
    boton(barra_lateral,"PACIENTES",40,  370,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))

    # INFORMACION

    label(barra_lateral,"ADMINISTRAR INFORMACION",30, 420, COLOR_BLANCO, COLOR_PRINCIPAL)
    boton(barra_lateral,"USUARIO", 40,470,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))
    boton(barra_lateral,"PACIENTES", 40,520,COLOR_BLANCO, COLOR_PRINCIPAL,"flat",150,25, comando=lambda: mostrar_frame(frame_principal_admin))

    # VENTANA PRINCIPAL

    tk.Button(ventana_principal_admin,
              text="<= VENTANA PRINCIPAL",
              font=("Sans-Serif", 7, "bold"),
              fg=COLOR_BLANCO, bg=COLOR_OSCURO,
              activebackground=COLOR_PRINCIPAL,
              activeforeground=COLOR_BLANCO,
              relief="flat", cursor="hand2",
              command=lambda: mostrar_frame(frame_principal_admin)).place(x=20, y=730, width=120, height=20)


    # Frame Ventana Principal
    frame_principal_admin = tk.Frame(ventana_principal_admin, bg="#FFFFFF")

    titulo_ventana_principal = tk.Label(frame_principal_admin,
                                        text="BIENVENIDO: ",
                                        font=("Sans-Serif", 30, "bold"),
                                        fg="#0097A7",
                                        bg="#FFFFFF")
    titulo_ventana_principal.place(x=270, y=70)

    _, tarjeta_pacientes_espera = tarjeta(frame_principal_admin, 105, 220, 340, 200,"PACIENTES EN\nESPERA", 18,24)
    _, tarjeta_pacientes_atendidos = tarjeta(frame_principal_admin, 555, 220, 340, 200,"PACIENTES\nATENDIDOS", 18,24)
    _, tarjeta_pacientes_urgencia = tarjeta(frame_principal_admin, 105, 460, 165, 150,"PACIENTES\nEN URGENCIA", 10, 18)
    _, tarjeta_pacientes_consulta = tarjeta(frame_principal_admin, 290, 460, 165, 150,"PACIENTES\nEN CONSULTA", 10, 18)
    tarjeta_fecha_hora, _ = tarjeta(frame_principal_admin, 555, 460, 340, 150, "", 10, 10, con_numero=False)

    label_fecha_hora = tk.Label(tarjeta_fecha_hora, text="",
                                font=("Sans-Serif", 14, "bold"),
                                fg=COLOR_OSCURO, bg=COLOR_CLARO,
                                justify="center")
    label_fecha_hora.place(relx=0, rely=0, relwidth=1, relheight=1)


    frame_principal_admin.place(x=251, y=0, relwidth=1,width=-251, relheight=1)


    # Frame Registrar Paciente
    frame_registrar_paciente = tk.Frame(ventana_principal_admin, bg="#FFFFFF")
    frame_registrar_paciente.place(x=251, y=0, relwidth=1,width=-251, relheight=1)

    actualizar_estadisticas()
    mostrar_frame(frame_principal_admin)


    ventana_principal_admin.mainloop()


ventana_principal_admin()
