nombre = input("Ingresá tu nombre y apellido: ")
nota1 = int(input("Ingresá tu calificación en el primer examen: "))
nota2 = int(input("Ingresá tu calificación en el segundo examen: "))
nota3 = int(input("Ingresá tu calificación en el tercer examen: "))

print(nombre,"posee un promedio de",(nota1 + nota2 + nota3) / 3,"en los 3 examenes")