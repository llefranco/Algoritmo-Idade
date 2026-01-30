imc = float(input("Digite seu IMC: "))
if (imc<=18.5):
    print ("Sua classificação de IMC é Abaixo do peso")
elif (imc<=24.9):
    print ("Sua classificação de IMC é Peso normal")
elif (imc<=29.9):
    print ("Sua classificação de IMC é Sobrepeso")
elif (imc<=39.9):
    print ("Sua classificação de IMC é Obesidade")
else:
    print ("Sua classificação de IMC é Obesidade Grave")