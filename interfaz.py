import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# ventana principal
"""ventana_principal = tk.Tk()
ventana_principal.geometry('1400x800')
ventana_principal.resizable(False, False)
ventana_principal.title('Home')
#ventana_principal.mainloop()"""


# ventana login
def login():

    ventana_login = tk.Tk()
    ventana_login.title("Login")
    ventana_login.geometry('1300x800')
    ventana_login.resizable(False, False)
    ventana_login.config(bg="#FFFFFF")
    icono_ventana_login = tk.PhotoImage(file="login.png")
    ventana_login.iconphoto(False, icono_ventana_login)

    canvas_fondo = tk.Canvas(ventana_login, width=650, height=800, bg="#0097A7")
    canvas_fondo.place(x=0, y=0)

    label_titulo_1 = tk.Label(ventana_login, text="CLI",
                             font=("Sans-Serif", 70,"bold"),
                             fg="#FFFFFF",
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


login()