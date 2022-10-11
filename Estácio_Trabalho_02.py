#Trabalho estácio_02
#Implementação do algoritmo de conversão
# de um número da base decimal para base binária
#Renan Matheus Linhares Abrantes


dividendo = int(input("Digite um Numero na Base decimal para ser convertido para binário: "))

dg = dividendo
quociente = 1
lista = []


while quociente >= 1:
    resto = dividendo%2
    lista.insert(0,resto)
    quociente = dividendo // 2
    dividendo = quociente


binario = ''.join([str(item) for item in lista])
print("O número",dg,", quando convertido em binário, vale:",binario)