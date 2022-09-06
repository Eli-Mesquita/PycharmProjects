from datetime import date
nome = str(input('Digite o seu nome completo:'))
sexo = str(input('Informe o sexo (M / F): ')).upper()
ano = int(input('Insira o seu ano de nascimento: '))
data = date.today().year
idade = data - ano
print(f'Olá, {nome}')
if sexo == 'F':
    print('Seu alistamento não é obrigatório.')
elif idade == 18:
    print(f'Quem nasceu em {ano} já tem ou fará {idade} anos de idade em {data}.\n'
          'Você deve alistar-se: \033[1;31mIMEDIATAMENTE.\033[m')
elif 18 > idade >= 1:
    menor = (18 - idade)
    print(f'Quem nasceu em {ano} já tem ou fará {idade} anos de idade em {data}. \n'
          f'Ainda faltam {menor} anos para o seu alistamento. \n'
          f'Seu alistamento será em {data+menor}')
elif idade == 0:
    rn = idade + 1
    pa = data + 1
    print(f'Quem nasceu em {ano} fara 1 ano em {pa}. \n'
         f'Ainda faltam 18 anos para o seu alistamento. \n'
         f'Seu alistamento será em {data + 18}')
elif idade > 18:
    maior = idade - 18
    print((f'Quem nasceu em {ano} já tem ou fará {idade} anos de idade em {data}. \n'
          f'Você deveria ter se alistado há {maior} anos. \n'
          f'Seu alistamento foi em {data-maior}'))
elif ano > data:
    print('Digite um ano de nascimento menor ou igual a data atual.')






