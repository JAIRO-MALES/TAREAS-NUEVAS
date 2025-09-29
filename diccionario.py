#Creamos el diccionario con la informacion sugerida#
informacion_personal = {
    "nombre": "Jairo Males",
    "edad": 37,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Cambiamos la clave
informacion_personal["ciudad"] = "Otavalo"

# Cambiamos la clave
informacion_personal["profesion"] = "Electronico"

# Verificaos si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0980471143"

# Eliminamos edad
del informacion_personal["edad"]

# vemos la informacion
print(informacion_personal)