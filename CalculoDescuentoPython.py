def calcular_descuento(monto_total, porcentaje_descuento=12):

    descuento = monto_total*(porcentaje_descuento / 100)
    return descuento

print("Calculador de descuentos")

# Primera llamada: aplica 12% por defecto

monto1 = float(input("Ingrese el monto de la primera compra: "))
descuento1 = calcular_descuento(monto1)
final1 = monto1 - descuento1
print(f"Compra 1: Monto = ${monto1}, Descuento = ${descuento1:.2f}, Total a pagar = ${final1:.2f}\n")

# Segunda llamada: monto y descuento aplicable
monto2 = float(input("Ingrese el monto de la segunda compra: "))
porcentaje2 = float(input("Ingrese el porcentaje de descuento: "))
descuento2 = calcular_descuento(monto2, porcentaje2)
final2 = monto2 - descuento2
print(f"Compra 2: Monto = ${monto2}, Descuento = ${descuento2:.2f}, Total a pagar = ${final2:.2f}")