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
lista_nome = []

while True: # Um  loop infinito, que é o ideal para mim nesse caso
        n = input("Digite seu nome: ")
        lista_nome.append(n)
        letra_maiscula = n.capitalize()
        if not n.isalpha():
            print("Só letras.")
        elif len(n) < 3:
            print("Nome muito curto.")
            continue
        else:
            break
    
"""
Aqui abaixo começa a coleta da str converte para int e add na lista
"""
lista_ano = []

while True:

    # Aqui o programa coleta uma string que é adicionada na lista
    ano_nascimento = input("Digite o ano de nascimento: ")

    if len(ano_nascimento) == 4:
        lista_ano.append(ano_nascimento)
        ano_nascimento = int(ano_nascimento) # Tive que converter, o len não converteu no if. - ???
        ano_atual = 2020
        idade = ano_atual - ano_nascimento
        
        print(f"{letra_maiscula} tem {idade} Anos!") # printando a variável {n} que é na verdade a função nome().
        break
        
    elif len(ano_nascimento) != 4 or len(ano_nascimento) == "".isnumeric():
        print("Apenas 4 digitos numericos.")





