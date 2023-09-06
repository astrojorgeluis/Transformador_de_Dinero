monto = int(input("Ingresa tu monto en pesos: "))
print('Monto ingresado: ',monto)
print("Billetes de 20.000: ", (monto//20000))
monto = monto%20000
print("Billetes de 10.000: ", (monto//10000))
monto = monto%10000
print("Billetes de 5.000: ", (monto//5000))
monto = monto%5000
print("Billetes de 2.000: ", (monto//2000))
monto = monto%2000
print("Billetes de 1.000: ", (monto//1000))
monto = monto%1000
print("Monedas de 500: ", (monto//500))
monto = monto%500
print("Monedas de 100: ", (monto//100))
monto = monto%100
print("Monedas de 50: ", (monto//50))
monto = monto%50
print("Monedas de 10: ", (monto//10))
monto = monto%10
print("Monedas de 5: ", (monto//5))
monto = monto%5
