# Programa que identifica los multiplos de 2 y 3 y los asigna a un grupo

print("----- Identificar multiplos de 2 y 3 y asignarlos a un grupo")

multiplos_2 = []
multiplos_3 = []

for numero in range(1, 100):
    if numero % 2 == 0:
        multiplos_2.append(numero)
    if numero % 3 == 0:
        multiplos_3.append(numero)

# Mostrar el resultado al final
print("✅ Múltiplos de 2:", multiplos_2)
print("✅ Múltiplos de 3:", multiplos_3)