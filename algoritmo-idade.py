'''
Dona Maria precisa de um algoritmo que faça as seguintes decisões:

1. Se a idade for menor que 12, deve mostrar a mensagem "CRIANÇA"

2. Se a idade for menor que 18, deve mostrar a mensagem "ADOLESCENTE"

3. Se a idade for menor que 60, deve mostrar a mensagem "ADULTO"

4. Se a idade não for nenhuma dessas condições, deve mostrar a mensagem "IDOSO"
'''

# Entrada de informação
idade = int(input ("Digite a idade: "))

if (idade<12):
    print("CRIANÇA")
elif (idade<18):
    print("ADOLESCENTE")
elif (idade<60):
    print("ADULTO")
else:
    print ("IDOSO")


