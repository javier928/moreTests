name = input("Dime tu nombre, por favor: ")
print(f"Hola {name}. Vamos a hacer un test de 7 preguntas sobre Microsoft Windows y Cine.")
puntos = 0

# Pregunta 1: Comando Copy
xx = input("1. El comando copy sirve para copiar archivos. (V/F)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes un punto.")
    puntos = puntos + 1

# Pregunta 2: Comando Dir
xx = input("2. El comando dir sirve para ver los archivos de una carpeta. (V/F)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes un punto.")
    puntos = puntos + 1

# Pregunta 3: El puente de los espías (Nueva ubicación)
xx = input("3. El personaje de la película El puente de los espías se llama Thomas Hanks. (V/F)?: ")
if xx.upper() == "V":
    print("Respuesta correcta. Tienes un punto.")
    puntos = puntos + 1

# Pregunta 4: Thomas Hanks (Opción múltiple)
print("4. ¿Qué película muy famosa ha protagonizado Thomas Hanks?")
print("A) Forrest Gump\nB) Titanic\nC) Avatar")
xx = input("Elige una opcion: (A/B/C): ")
if xx.upper() == "A":
    print("¡Correcto! Forrest Gump.")
    puntos = puntos + 1

# Pregunta 5: Meryl Streep (Récord)
xx = input("5. ¿Es Meryl Streep la actriz con más nominaciones a los Oscar de la historia? (V/F)?: ")
if xx.upper() == "V":
    print("¡Correcto! Tiene el récord con 21 nominaciones.")
    puntos = puntos + 1

# Pregunta 6: El Orfanato
xx = input("6. ¿Es Belén Rueda el personaje principal de la película española El Orfanato? (V/F)?: ")
if xx.upper() == "V":
    print("¡Respuesta correcta!")
    puntos = puntos + 1

# Pregunta 7: La casa de los espíritus
xx = input("7. El personaje de la película La casa de los espíritus se llama Meryl Streep. (V/F)?: ")
if xx.upper() == "V":
    print("Respuesta correcta.")
    puntos = puntos + 1

print("---------------------------")
print(f"Test finalizado. {name}, tu nota final es: {puntos} sobre 7.")