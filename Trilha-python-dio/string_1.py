nome = "marcos"

print(nome.upper()) # fica todo em  maiusculo 
print(nome.lower()) # fica todo em minusculo
print(nome.title()) # fica só com a primeira letra em maiusculo 

texto = "  ola mundo!   "

print(texto + ".")
print(texto.strip() + ".") #cortatodo espaço em branco
print(texto.rstrip() + ".") # corta o espaço em branco da  direita
print(texto.lstrip() + ".") # corta o espaço em branco da esquerda 

menu = "python"

print("#####python#####")
print(menu.center(20)) #Coloca o valor da careavel no centro e  acrescenta espaço em branco
print(menu.center(20, "#"))#no centro e  acrescenta o carectere desejado
print("-".join(menu))# colocando traço no nome letra por letra

for letra in menu:
    print(letra, end="-")