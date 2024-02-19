while True:
    print("""Benvinguts a pycalc, introduiu una de les següents opcions:
0. Sortir
1. Sumar
2. Restar
3. Multiplicar
4. Dividir""")
    num = input("Digues un numero: ")
    if num == "0":
        break
    if num == "1":
        num1 = float(input("Introdueix un numero: "))
        num2 = float(input("Introdueix un altre numero: "))
        resultat = num1 + num2
        print("El resultat és: ", resultat)
    if num == "2":
        num1 = float(input("Introdueix un numero: "))
        num2 = float(input("Introdueix un altre numero: "))
        resultat = num1 - num2
        print("El resultat és: ", resultat)
    if num == "3":
        num1 = float(input("Introdueix un numero: "))
        num2 = float(input("Introdueix un altre numero: "))
        resultat = num1 * num2
        print("El resultat és: ", resultat)
    if num == "4":
        num1 = float(input("Introdueix un numero: "))
        num2 = float(input("Introdueix un altre numero: "))
        if num2 == 0.0:
            print("El resultat és infinit.")
        else:
            resultat = num1 / num2
            print("El resultat és: ", resultat)
