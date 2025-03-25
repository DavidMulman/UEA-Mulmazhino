# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "David Mulman",
    "edad": 17,
    "ciudad": "Lago Agrio",
    "profesion": "ALBAÑIL"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Pacayacu"  # Cambiar la ciudad

# Agregar una nueva clave-valor al diccionario que represente la "profesion"
informacion_personal["profesion"] = "tecnologo en TIC"  # Actualizar profesión

# Verificar si la clave "telefono" existe en el diccionario y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"  # Número ficticio

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad")

# Imprimir el diccionario final
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
