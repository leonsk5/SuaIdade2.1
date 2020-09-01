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

i = 0
while i < 1: # ainda não solucionado o problema do loop
  
        def nome(nome = input("Digite seu nome: ")):
                lista_nome.append(nome)
                if nome == None:
                        print("Digite alguma coisa.")
                elif not nome.isalpha():
                        print("Apenas letras.")
                elif len(nome) < 3:
                        print("Nome muito curto.")
                return nome
        i = i + 1
nome()
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
        
        print(f"{nome()} tem {idade} Anos!") # printando a variável {n} que é na verdade a função nome().
        break
        
    elif len(ano_nascimento) != 4 or len(ano_nascimento) == "".isnumeric():
        print("Apenas 4 digitos numericos.")





