produtos = ['bolo', 'pudim', 'agua']
quantidades = [20, 30, 40]
historico = []


def add_produto():
    produtos.append(input('Qual produto desejá adicinar: '))
    quantidades.append(input('Qual a quantidade desse produto: '))
    add01 = (f'{quantidades[-1]} unidades do produto {produtos[-1]} foi adicionado ao estoque!')
    print(add01)
    historico.append(add01)
    print(historico)
    ask()


def find_product(nome_produto):
    print(f'{nome_produto}')
    #produto = list.index({nome_produto})
    #return produto


def remove_produto():
    print('=================')
    print('Digite 1 para cancelar')
    res1 = input('Qual produto desejá remover: ')
    if res1 == '1':
        print('=================')
        ask()
    if res1 in produtos:
        find_product(res1)
        print(f'Produto encontrado!')
        print('=================')
        print('Digite 1 para cancelar')
        res2 = int(input('Qual a quantidade deseja remover: '))
            
        if res2 == 1:
            ask()
    else:
        print('Produto não encontrado')
        print('Tente novamente')
        remove_produto()
    print('Item Removido')


def ask():
    print('1. Adicionar produto')
    print('2. Remover produtos em estoque')
    print('3. Ver Produtos')
    print('4. Historio de transções')
    res = int(input('Escolha uma das opções: '))
    if res == 1:
        add_produto()
    elif res == 2:
         remove_produto()
    else:
        print('Resposta invalida!!')
        print('Tente novamente!')
        ask() 
    
        


ask()






