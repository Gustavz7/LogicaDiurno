print("bienvenid@ a calculadora.py v1.0")

valor1=int(input("primer valor = "))
valor2=int(input("segundo valor = "))

print('''"---eliga una opcion---"   
suma = a
resta = b
multiplicacion = c
division = d ''')

operacion=(input())
if operacion=="a":
    resultado=valor1+valor2
    print("el resultado de la operacion es :", resultado)
elif operacion == "b":
    resultado = valor1 - valor2
    print("el resultado de la operacion es :", resultado)
elif operacion == "c":
    resultado = valor1 * valor2
    print("el resultado de la operacion es :", resultado)
elif operacion == "d":
    resultado= valor1/valor2
    print("el resultado de la operacion es :", resultado)




