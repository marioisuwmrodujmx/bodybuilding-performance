exercise = input("ejercicio: ")
weight = float(input("peso (kg): "))
reps = float(input("repeticiones: "))
print("Has registrado: ")
print(exercise, "-", weight, "kg x", reps, "reps")
volume = weight * reps
print("volumen de entrenamiento: ", volume)