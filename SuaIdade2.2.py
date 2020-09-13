"""
Programa  coleta dados do usuário coletando uma str e add em uma lista, depois
convertendo para int.
ABAIXO CRIEI UM PSEUDOCÓDIGO, APESAR DE EXISTER MILHARES. PARA MELHORAR MEU ENTENDIMENTO!
                           # coletar str
                           list:
                           def:input:
                           if:
                           elif:
                           
                           # coletar int
                           while:
                           if:
                           append:
                           int:
                           print:
                           break:
                           elif
                           

"""
"""
ATUALIZADO PARA FUNCIONAR COM UMA FUNÇÃO
LÓGICO TEM BUGS, QUE SERÃO CORRIGIDOS COM O TEMPO!

"""

def suaIdade(nome, ano_nascimento): 
    lista_nome = [] # lista para adicionar o nomes.
    lista_ano_nascimento = [] # adicionar anos nascimento.
    
    while True: 
        nome = input("Digite seu nome: ")
        lista_nome.append(nome) # add input usuário como um string na lista.
        l_maiuscula = nome.capitalize()
        
        if not nome.isalpha():
            print("apenas letras")
        elif len(nome) < 3:
            print("Nome muito curto.")
            continue
        else:
            break
    while True:
        ano_nascimento = input("Digite Ano de Nascimento: ") 
        lista_ano_nascimento.append(ano_nascimento) # add input usuário com um string na lista

        if len(ano_nascimento) == 4:
            ano_atual = 2020
            ano_nascimento = int(ano_nascimento) # conversão de string para int
            idade = ano_atual - ano_nascimento
            print(f"{nome} tem {idade} Anos.", lista_nome, lista_ano_nascimento)
            break

        elif len(ano_nascimento) != 4 or len(ano_nascimento) == "".isnumeric():
            print("Apenas 4 digitos numericos.")
            continue
        return nome, ano_nascimento
suaIdade(nome=1, ano_nascimento=2)







