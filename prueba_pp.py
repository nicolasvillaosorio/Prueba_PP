from collections import defaultdict
import heapq
from datetime import datetime

from tkinter import Tk, Label, Button, StringVar, OptionMenu,Frame
from tkcalendar import Calendar




#air_ports= ["BOG", "MDE", "BAQ", "BGA", "SMR", "CTG", "CLO", "EOH"]

itinerario = {"LUNES":[
    ("BOG" , "MDE", 60),
    ("BOG" , "BAQ", 90),
    ("MDE" , "CTG", 75),
    ("MDE" , "BGA", 75),
    ("CTG" , "CLO", 45),
    ("CTG" , "SMR", 180),
    ("SMR" , "BAQ", 60)],

    "MARTES":[
    ("MDE" , "CTG", 75),
    ("MDE" , "BGA", 75),
    ("CTG" , "CLO", 45),
    ("BOG" , "BGA", 35),
    ("SMR" , "CLO", 130),
    ("SMR" , "EOH", 80),
    ("CLO" , "BAQ", 25)
    ],

    "MIERCOLES":[
    ("BOG" , "MDE", 60),
    ("CLO" , "BAQ", 25),
    ("EOH" , "BGA", 60),
    ("MDE" , "BAQ", 45),
    ("MDE" , "SMR", 50),
    ("BAQ" , "CTG", 30),
    ("BGA" , "CLO", 45)
    ],

    "JUEVES":[
    ("MDE" , "BAQ", 45),
    ("BAQ" , "SMR", 60),
    ("BGA" , "CTG", 100),
    ("SMR" , "CLO", 130),
    ("CTG" , "EOH", 50),
    ("BOG" , "EOH", 60),
    ("CLO" , "MED", 120)
    ],

    "VIERNES":[
    ("BOG" , "BAQ", 90),
    ("MDE" , "EOH", 10),
    ("SMR" , "BGA", 110),
    ("CTG" , "BOG", 100),
    ("CLO" , "BAQ", 25),
    ("EOH" , "BGA", 60),
    ("CTG" , "SMR", 180)
    ],

    "SABADO":[
    ("BOG" , "SMR", 60),
    ("MDE" , "CTG", 75),
    ("BAQ" , "EOH", 50),
    ("EOH" , "MDE", 10),
    ("CTG" , "SMR", 180),
    ("BOG" , "MDE", 60),
    ("MDE" , "BAQ", 45)
    ],

    "DOMINGO":[
    ("BOG" , "EOH" ,60),
    ("MDE" , "BAQ" ,45),
    ("SMR" , "CTG", 180),
    ("BGA" , "MDE", 75),
    ("CLO" , "BOG", 25),
    ("EOH" , "BAQ", 50),
    ("CTG" , "BGA", 100)
    ]

}

grafo_vuelos= defaultdict(dict)

# for origin, destination, time in flights:
#     grafo_vuelos_por_dia[origin].append((destination, time))
#     grafo_vuelos_por_dia[destination].append((origin, time))


for dia, vuelos in itinerario.items():

    aux_grafo = defaultdict(list) 
    
    for origen, destino, duracion in vuelos:
        aux_grafo[origen].append((destino, duracion))
        aux_grafo[destino].append((origen, duracion))  
    grafo_vuelos[dia] = aux_grafo  

#print(grafo_vuelos_por_dia)
#print(grafo_vuelos_por_dia["LUNES"])

def rutasDijkstra(grafo, origen, destino):
    cola_prioridad = [(0, origen, [])] 
    rutas = []

    while cola_prioridad:

        duracion_actual, aeropuerto_actual, ruta_actual = heapq.heappop(cola_prioridad)
        ruta_actual = ruta_actual + [aeropuerto_actual]
        
        if aeropuerto_actual == destino:
            rutas.append((duracion_actual, ruta_actual))
            continue

        for vecino, duracion in grafo[aeropuerto_actual]:
            if vecino not in ruta_actual:  
                nueva_duracion = duracion_actual + duracion
                heapq.heappush(cola_prioridad, (nueva_duracion, vecino, ruta_actual))

    rutas_ordenadas = sorted(rutas, key=lambda x: x[0])
    return rutas_ordenadas


def rutasTotales(dia, origen, destino):
    if dia not in grafo_vuelos:
        return(f"No hay datos de vuelos para el día {dia}.")

    ret_rutas=''
    grafo = grafo_vuelos[dia]
    rutas_ordenadas = rutasDijkstra(grafo, origen, destino)

    if (origen == destino) or (origen == "Org") or (destino== "Dest"):
        return("Seleccione una ruta valida")

    if rutas_ordenadas:
        ret_rutas = f"Las rutas de {origen} a {destino} el {dia}, ordenadas por duración son:\n\n"
        for duracion_total, ruta in rutas_ordenadas:
            ret_rutas += f"Ruta: {' a '.join(ruta)} con duración total de {duracion_total} minutos.\n"
        return ret_rutas
    else:
        return(f"No existe una ruta de {origen} a {destino} en {dia}.")


def diaSemana(fecha):
    fecha_obj = datetime.strptime(fecha, "%Y-%m-%d")
    dias=["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]
    dia_semana = dias[fecha_obj.weekday()]
    #fecha_obj.strftime("%A").upper()
    return dia_semana

def seleccionDia():
    fecha = calendario.get_date()
    dia = diaSemana(fecha)
    return dia
    #res.config(text=f"El día de la semana es: {dia}")

def seleccionOrigenDestino():
    origen= ciudad_origen.get()
    destino= ciudad_destino.get()
    return origen, destino

def llamaSelectores():
    dia= seleccionDia()
    origen, destino = seleccionOrigenDestino()
    #rutasTotales(dia, origen, destino)
    frame_rutas.config(text=rutasTotales(dia, origen, destino))


############
############
ventana = Tk()
ventana.title("Punto de Pago Air")
ventana.geometry("500x700")
ventana.config(bg="white")

import os, sys

if getattr(sys, 'frozen', False):
    path = sys._MEIPASS
else:
    path = os.path.abspath(".")

icon_path = os.path.join(path, 'puntopago.ico')
ventana.iconbitmap(icon_path)
#ventana.iconbitmap(default='../Prueba_PP/puntopago.ico', bitmap='../Prueba_PP/puntopago.ico')

label_titulo= Label(ventana, text="Bienvenido a Punto Pago Air", font=("Verdana",15, "bold"), foreground="#003366", bg="white")
label_titulo.pack(pady=18)



frame_ciudades= Frame(ventana)
frame_ciudades.pack(pady=20)
frame_ciudades.config(bg="white")

############
ciudad_origen = StringVar()
ciudad_origen.set("Org")  

ciudad_destino = StringVar()
ciudad_destino.set("Dest")  

####################

label_origen= Label(frame_ciudades, text="Seleccione el aeropuerto de origen", font=("Verdana", 9, "bold") , foreground="#4D4D4D", bg="white", wraplength=150)
#label_origen.pack( side='left')
label_origen.grid(row=0, column=0, padx=5)

menu_origen = OptionMenu(frame_ciudades, ciudad_origen, "BOG", "MDE", "BAQ", "BGA", "SMR", "CTG", "CLO", "EOH")
menu_origen.grid(row=1, column=0, padx=5)

###################

label_destino= Label(frame_ciudades, text="Seleccione el aeropuerto de destino", font=("Verdana",9, "bold"),foreground="#4D4D4D", bg="white", wraplength=150)
label_destino.grid(row=0, column=1, padx=5)

menu_destino = OptionMenu(frame_ciudades, ciudad_destino, "BOG", "MDE", "BAQ", "BGA", "SMR", "CTG", "CLO", "EOH")
menu_destino.grid(row=1, column=1, padx=5)


##############################

label_calendario= Label(ventana, text="Por favor seleccione la fecha de viaje", font=("Verdana",10, "bold"), bg="white")
label_calendario.pack(pady=10)

calendario = Calendar(ventana, selectmode="day", date_pattern="yyyy-mm-dd", font=("Verdana",8, "bold"), mindate=datetime.now(), locale= "es")
calendario.pack(pady=5)

#######################
dia_seleccion = Button(ventana, text="Aceptar", command=llamaSelectores, font=("Verdana",10, "bold"), foreground="#007ACC", bg="white", activebackground="#007ACC", activeforeground="white")
dia_seleccion.pack(pady=20)

###################################
frame_rutas = Label(ventana, font=("Verdana",10, "bold"), justify= 'left',  wraplength=450, foreground="#333333", bg="white")
frame_rutas.pack(pady=10)


# Ejecutar la interfaz
ventana.mainloop()

