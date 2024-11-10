##### _NOTA:  Este aplicativo cuenta con un archivo ejecutable para mejorar la interaccion con el usuario, dicho ejecutable se encuentra dentro de la carpeta "dist"_

# MANUAL DE USUARIO PARA APLICATIVO **PUNTO DE PAGO AIR**

Este software le permite a los usuarios visualizar las rutas de vuelos disponibles a partir de una ciudad de origen, una ciudad de destino y una fecha tentativa de viaje.

![image](https://github.com/user-attachments/assets/96790eda-d19e-45d0-b596-bc51e30ccf7f)






Para esto es necesario seleccionar: 
  1. Ciudad de origen.

     ![image](https://github.com/user-attachments/assets/28449011-8c5d-4ef4-81e0-4da47ea6c10e)




  2. Ciudad de destino.

      ![image](https://github.com/user-attachments/assets/3c6f2ed1-cef0-4d1e-9e5d-33504d723c59)




  3. Fecha (Mes,año,día)
  
     ![calendario](https://github.com/user-attachments/assets/26424e3f-c108-47f8-889a-3db0eb6dae06)


 
  4. Dar click en botón "Aceptar".

     ![aceptar](https://github.com/user-attachments/assets/42bd2ae9-576a-4699-865d-b50dff554036)





Teniendo como resultado las rutas de vuelo, incluyendo sus respectivas escalas (si las hay) y la duración total del trayecto. La primera ruta mostrada será la de menor tiempo de viaje.

  ![resultado](https://github.com/user-attachments/assets/8520e474-7ff4-4587-b643-4344385f5c23)




# IMPLEMENTACION

  ## ALGORITMO PRINCIPAL

  Debido a que el sistema de aeropuertos indicaba que no estaba disponibles todos los vuelos directos entre todas las ciudades, se concluyó que el problema debía resolverse mediante un grafo; dado que era necesario devolver todas las rutas posibles para llegar a un destino, ordenadas por el tiempo requerido por cada ruta, se optó por recorrer el grafo utilizando el algoritmo Dijkstra; para simplificar, se asumió tamiben, que los vuelos eran bidireccionales; es decir, un vuelo de BOG a CTG implica un vuelo de regreso de CTG a BOG.

  ### ALGORITMO DIJKSTRA
  "El algoritmo de Dijkstra, también llamado algoritmo de caminos mínimos, es un algoritmo para la determinación del camino más corto dado un vértice origen al resto de los vértices en un grafo con pesos en cada arista." [1]




  ![image](https://github.com/user-attachments/assets/41b66673-f99d-4f2a-826e-da3835179b28)

  ## INTERFAZ
  La interfaz grafica se desarrolló utilizando el paquete Tkinter disponible en Python, a traveés de sus modulos de etiquetas de texto, cuadros, menus desplegables, botones, herramienta calendario, entre algunos otros

  ### TKINTER
  "El paquete tkinter («interfaz Tk») es la interfaz por defecto de Python para el kit de herramientas de GUI Tk. Tanto Tk como tkinter están disponibles en la mayoría de las plataformas Unix, así como en sistemas Windows (Tk en sí no es parte de Python, es mantenido por ActiveState)."[2]
  

## EJECUTABLE
  Finalmente con el modulo pyinstaller se generó un archivo ejecutable para la aplicación

  ### PYINSTALLER

  "PyInstaller lee un script Python escrito por ti. Analiza tu codigo para encontrar cada modulo o libreria que tu codigo necesita para ejecutarse. Luego almacena copias de estos archivos - ¡incluyendo el interprete de Python! - y los coloca con tu script en una unica carpeta, u optionalmente en un unico archivo ejecutable."[3]



## REFERENCIAS
  [1] https://atlas.uned.es/algoritmos/voraces/dijkstra.html#:~:text=El%20algoritmo%20de%20Dijkstra%2C%20tambi%C3%A9n,por%20primera%20vez%20en%201959

  [2] https://docs.python.org/es/3/library/tkinter.html

  [3] https://pyinstaller.org/en/stable/operating-mode.html
