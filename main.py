#lista = ["python", "c++", "ruby", "kotlin"]

#for x in lista: 
    #print(x) printa pulando a linha em cada acesso a lista
    #print(x, end=" ") # printa colocando no final de cada acesso um espaço, sem pular a linha

"""lista_npcs = [
    {"name": "Monstro 1", "level": 1},
    {"name": "Monstro 2", "level": 2},
    {"name": "Monstro 3", "level": 3},
    {"name": "Monstro 4", "level": 4},
    {"name": "Monstro 5", "level": 5},
]

#print(lista_npcs[0] ['name'], "level:", lista_npcs[0] ['level'])
for npc in lista_npcs:
    #print(npc["name"], npc["level"])
    print(f"Nome: {npc['name']} // Level: {npc['level']}")
"""
"""
Coleções no python (fonte https://www.devmedia.com.br/colecoes-no-python-listas-tuplas-e-dicionarios/40678):

    Lista:
        lista = ['elemento1', 'elemento2', 'elemento3']
        print(type(lista)) # type 'list'
        print(len(lista)) # 3
        print(lista[2]) # elemento3
        
        adicionar elementos na lista:
            lista.append('elemento4') # adiciona um elemento no final da lista
            print(lista) # ['elemento1', 'elemento2', 'elemento3', 'elemento4']

            lista.insert(1, 'elemento1.5') # adiciona um elemento em uma posição da lista insert(posição, elemento)
            print(lista) # ['elemento1', 'elemento1.5', 'elemento2', 'elemento3']

        remover elementos na lista:
            lista.remove('elemento1.5') # remove pelo valor informado
            print(lista) # ['elemento1', 'elemento2', 'elemento3']

            lista.pop(0) # remove pelo índice do elemento
            print(lista) # ['elemento2', 'elemento3']
    
    Tupla:
        tupla = ('elemento1', 'elemento2', 'elemento3')
        print(type(tupla)) # class='tuple'
        print(tupla) # ('elemento1', 'elemento2', 'elemento3')
        print(tupla[2]) # elemento3

        obs1:
            tuplas é uma estrutura imutável, sem remoção ou adição
        obs2:
            tuplas de um único elemento necessita da colocação da vírgula no final do elemento para diferenciar
            de uma string, ex:
            
            objeto_string = ('tesoura')
            objeto_tupla = ('tesoura',)
            print(type(objeto_string)) # class 'str'
            print(type(objeto_tupla)) # class 'tuple'
    
    Dicionário: 
        dicionario = {
            'chave1': 'valor1',
            'chave2': 'valor2',
            'chave3': 'valor3'
        }

        print(dicionario[chave1]) # valor1

        adicionar elementos no dicionário:
            print(dicionario) # {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}

            dicionario['chave4'] = 'valor4'
            print(dicionario) # {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
        
        remover elementos no dicionário:
            print(dicionário) # {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3', 'chave4': 'valor4'}
            dicionario.pop('chave4', None)

            print(dicionario) # {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
            del dicionario['chave3']

            print(dicionario) # {'chave1': 'valor1', 'chave2': 'valor2'}

        Funções coleções:
            min() e max():
                numeros = [15, 5, 0, 20, 10]
                nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']

                print(min(numeros)) # 0  -> menor valor numérico
                print(max(numeros)) # 20    -> maior valor numérico
                print(min(nomes)) # Alex    -> primeira posição disponível na ordem alfabética
                print(max(nomes)) # Renata  -> ultima posição posível na ordem alfabética
            
            sum():
                numeros = [1, 3, 6]

                print(sum(numeros)) # 10 -> soma de todos os elementos, não funciona para string
            
            len():
                paises = ['Argentina', 'Brasil', 'Colômbia', 'Uruguai']

                print(len(paises)) # 4 -> total de itens da coleção

            type():
                professores = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
                estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
                cliente = {
                    'Nome': 'Fábio Garcia',
                    'email' : 'fabio_garcia_9@outlook.com'
                }

                print(type(professores)) # list
                print(type(estacoes)) # tuple
                print(type(cliente)) # dict
"""
from random import randint

lista_npcs = [] #criando a lista vazia

player = {
    "nome": "Victor",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

def criar_npc(level):

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level
    }
    #lista_npc.append(novo_npc)
    return novo_npc

def gerar_npcs(numero_npcs):
    for i in range(numero_npcs): # range transforam o numero inteiro em uma lista, ex range(5) = [0, 1, 2, 3, 4] 
        npc = criar_npc(i + 1)
        lista_npcs.append(npc)
        #lista_npc.append(criar_npc())

def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)

def exibir_npc(npc):
    print(f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // Vida: {npc['hp']}")

def exibir_player():
    print(f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // Vida: {player['hp']}/{player['hp_max']} // Exp: {player['exp']}/{player['exp_max']}")

def reset_player():
    player['hp'] = player['hp_max']

def reset_npc(npc):
    npc['hp'] = npc['hp_max']

def iniciar_batalha(npc):
    status_batalha = True
    while status_batalha== True:
        atacar_npc(npc)
        atacar_player(npc)
        exibir_info_batalha(npc)
        status_batalha = morreu(npc)

def atacar_npc(npc):
    npc['hp'] -= player['dano']

def atacar_player(npc):
    player['hp'] -= npc['dano']

def exibir_info_batalha(npc):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"NPC: {npc['nome']}: {npc['hp']}/{npc['hp_max']}\n")

def level_up():
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * player['level']
        player['hp_max'] = player['hp_max'] * player['level']  
        print(f"Parabéns, você atingiu o level {player['level']}\n")

def morreu(npc):
    if(player['hp'] <= 0):
        print(f"O {player['nome']} morreu")
        exibir_npc(npc)
        return False
    
    elif(npc['hp'] <= 0):
        print(f"O {npc['nome']} morreu\nVocê ganhou {npc['exp']} de experiência")
        
        player['exp'] += npc['exp']
        level_up()
        
        exibir_player()
        
        reset_player()
        reset_npc(npc)
        return False
    return True

def main():
    numero_oponentes = randint(5,15)
    
    gerar_npcs(numero_oponentes)

    npc_selecionado = lista_npcs[0]
    vezes = 0
    while vezes < 50:
        iniciar_batalha(npc_selecionado)
        vezes += 1
        

main()