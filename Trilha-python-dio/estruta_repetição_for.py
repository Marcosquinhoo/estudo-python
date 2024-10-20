texto = input("informe um texto")
VOGAS ="AEIOU"

#exemplo usando um iterável
for letra in texto:
    if letra.upper() in VOGAS:
        print(letra, end="")
        
else:        
    print()
    print("final do laço ")
    
    
    #exemplo utilizando a função built-in range
    for numero in range(0, 51, 5):
        print(numero, end=" ")