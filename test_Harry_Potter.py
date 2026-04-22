xname = input("Dime tu nombre, por favor: ")
print(f"Hola {xname}, vamos a hacer un test sobre cultura general.")
puntos = 0

# Pregunta 1
xx = input("1. El comando COPY sirve para copiar archivos (v/f)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes 1 punto.")
    puntos = puntos + 1

# Pregunta 2
xx = input("2. El comando DIR sirve para ver los archivos de una carpeta (v/f)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes 1 punto.")
    puntos = puntos + 1

# Pregunta 3
xx = input("3. ¿La princesa Leia es un personaje de Star Wars (v/f)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes 1 punto.")
    puntos = puntos + 1

# Pregunta 4 (Convertida a V/F)
xx = input("4. ¿Harrison Ford es el actor que interpreta a Han Solo (v/f)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes 1 punto.")
    puntos = puntos + 1

# Pregunta 5 (Convertida a V/F)
xx = input("5. ¿Emma Watson interpretó a Hermione Granger en Harry Potter (v/f)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes 1 punto.")
    puntos = puntos + 1

print("---------------------------------")
print(f"{xname}, tu nota final en este test es: {puntos} de 5.")
