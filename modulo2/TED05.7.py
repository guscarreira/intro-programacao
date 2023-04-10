print("TED 5 | QUESTÃO 7 - MESSIAS")
quantidade = int(input('Quantas pessoas você quer cadastrar? '))
cadastro = []
for c in range(quantidade):
    print('')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Informe sua idade: '))
    email = str(input('Digite seu email: '))
    cadastro.append({'nome': nome, 'idade': idade, 'email': email})

print("Cadastro:")
for item in cadastro:
    print("Nome:", item['nome'])
    print("Idade:", item['idade'])
    print("E-mail:", item['email'])
    print("")