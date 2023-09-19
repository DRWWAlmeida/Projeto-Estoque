produtos = []
quantidades = []
historico = []


def add_produto():
        produtos.append(input('Qual produto desejá adicinar: '))
        quantidades.append(input('Qual a quantidade desse produto: '))
        add01 = (f'{quantidades[-1]} unidades do produto {produtos[-1]} foi adicionado ao estoque!')
        print(add01)
        historico.append(add01)
        print(historico)
        ask()


def ask():
    print('1. Adicionar produto')
    print('2. Realizar ajuste de estoque')
    print('3. Ver Produtos')
    print('4. Historio de transções')
    res = input('Escolha uma das opções: ') 
    if res in valid_codes:
        pass
    else:
        print('Resposta invalida!!')
        print('Tente novamente!')
        ask() 
    if int(res) == 1:
        add_produto()
        


valid_codes = ["1", "2", "3", "4"]
ask()






