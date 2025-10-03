ruta = 'C:/Users/JAIRO/Documents/TAREAS-NUEVAS/my_notes.txt'
archivo = open(ruta, 'r')

print(archivo.readline())
print(archivo.readline())
print(archivo.readline())

archivo.close()