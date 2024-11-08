from collections import defaultdict
import heapq
from datetime import datetime

from tkinter import Tk, Label, Button, StringVar, OptionMenu,Frame
from tkcalendar import Calendar




#air_ports= ["BOG", "MDE", "BAQ", "BGA", "SMR", "CTG", "CLO", "EOH"]

itinerario = {"LUNES":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45),
    ("CTG", "BOG", 180)],

    "MARTES":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45)],

    "MIERCOLES":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45)],

    "JUEVES":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45)],

    "VIERNES":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45)],

    "SABADO":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45)],

    "DOMINGO":[
    ("BOG", "MDE", 60),
    ("BOG", "BAQ", 90),
    ("MDE", "CTG", 75),
    ("CTG", "BAQ", 45)]

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

    if rutas_ordenadas:
        ret_rutas = f"Todas las rutas de {origen} a {destino} en {dia}, ordenadas de menor a mayor duración:\n\n"
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
ventana.geometry("600x600")

frame_ciudades= Frame(ventana)
frame_ciudades.pack(pady=30)

############
ciudad_origen = StringVar()
ciudad_origen.set("Seleccion")  

ciudad_destino = StringVar()
ciudad_destino.set("Seleccion")  

####################

label_origen= Label(frame_ciudades, text="Seleccione el Origen")
#label_origen.pack( side='left')
label_origen.grid(row=0, column=0, padx=5)

menu_origen = OptionMenu(frame_ciudades, ciudad_origen, "BOG", "MDE", "BAQ")
menu_origen.grid(row=1, column=0, padx=5)

###################

label_destino= Label(frame_ciudades, text="Seleccione el Destino")
label_destino.grid(row=0, column=1, padx=5)

menu_destino = OptionMenu(frame_ciudades, ciudad_destino, "BOG", "MDE", "BAQ")
menu_destino.grid(row=1, column=1, padx=5)


##############################

label_calendario= Label(ventana, text="Por favor seleccione la fecha de viaje")
label_calendario.pack(pady=10)

calendario = Calendar(ventana, selectmode="day", date_pattern="yyyy-mm-dd")
calendario.pack(pady=5)

#######################
dia_seleccion = Button(ventana, text="Seleccionar Fecha", command=llamaSelectores)
dia_seleccion.pack(pady=10)

###################################
frame_rutas = Label(ventana)
frame_rutas.pack(pady=10)


# Ejecutar la interfaz
ventana.mainloop()




# # Ejemplo de uso
# fecha = "2024-11-07"
# dia= diaSemana(fecha)
# origen="MDE"
# destino= "CTG"
# #print(dia)
# rutasTotales(dia, origen, destino)
