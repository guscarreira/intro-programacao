print("TED 5 | QUESTÃO 6 - MESSIAS")
print('='*70 )
convidados =('Fred Desimpedidos', 'Ricardo Alface', 'Larissa Santos', 'Bruna Griphao', 'Medina')

for convidado in convidados:
    print ('Olá,',convidado,',você foi convidado para minha festa!')
print('='*70)

desistentes = ('Gabriel Fop','Ricardo Alface')
for desistente in desistentes:
    print(f'{desistente} não irá comparecer a festa.')
print('='*70)

print('Key Alves e Gustavo Cowboy vão substituí-los.')
print('='*70)

convidados.remove('Medina')
convidados.remove('Ricardo Alface')
convidados.append('Key Alves')
convidados.append('Gustavo Cowboy')

for convidado in convidados:
    mensagem = f"Olá {convidado}, gostaria de informar que a festa foi confirmada e eu te aguardo lá. Vamos curtir!"
    print(mensagem)
print('='*70)