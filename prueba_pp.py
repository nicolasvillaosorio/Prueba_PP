from collections import defaultdict
import heapq




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
        print(f"No hay datos de vuelos para el día {dia}.")
        return None

    grafo = grafo_vuelos[dia]
    rutas_ordenadas = rutasDijkstra(grafo, origen, destino)

    if rutas_ordenadas:
        print(f"Todas las rutas de {origen} a {destino} en {dia}, ordenadas de menor a mayor duración:")
        for duracion_total, ruta in rutas_ordenadas:
            print(f"Ruta: {ruta} con duración total de {duracion_total} minutos.")
    else:
        print(f"No existe una ruta de {origen} a {destino} en {dia}.")






rutasTotales("LUNES", "MDE", "CTG")

