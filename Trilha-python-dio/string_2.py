nome = "Marcos"
idade = 32
profissao = "programador"
linguagem = "python"

print("Meu nome: %s, Minha idadade: %d.".format(nome, idade))

print("Nome: {}, Idade: {}, profisao: {}, linguagem: {}."
      .format(nome, idade, profissao, linguagem ))

print("Nome: {0} Idade: {1}".format(nome, idade))

print(f"Meu nome: {nome}, Minha idade: {idade}, Minha profissao: {profissao} a linguagem:  {linguagem}")

#formatar strings com f-string
pi = 3.14159

print(f"valor de PI: {pi:.2f}")
print(f"valor de OI: {pi:10.2f}")