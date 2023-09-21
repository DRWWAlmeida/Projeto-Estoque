produtos = ['bolo', 'pudim', 'agua']
quantidades = [20, 30, 40]
historico = []


def add_produto():
    print('=================')
    produtos.append(input('Qual produto desejá adicionar: '))
    quantidades.append(input('Qual a quantidade desse produto: '))
    historico.append(f'{quantidades[-1]} unidades do produto {produtos[-1]} foi adicionado ao estoque!')
    print(historico[-1])
    print('=================')
    ask()


def find_product(nome_produto):
    prod_found = produtos.index(nome_produto)
    return prod_found
    

def find_quanti(quantidade_produtos):
    quanti_found = quantidades[quantidade_produtos]
    return quanti_found


def remove_produto():
    print('=================')
    print('Digite "cancelar" para voltar!')
    res1 = input('Qual produto desejá remover: ')
    if res1 == 'cancelar':
        print('=================')
        ask()
    if res1 in produtos:
        prod_found = find_product(res1)
        quanti_found = find_quanti(prod_found)
        if quanti_found > 0:
            pass
        else:
            print('O estoque do produto é 0')
            remove_produto()
        print('=================')
        print('Digite "cancelar" para voltar!')
        res2 = input('Qual a quantidade deseja remover: ')
        if res2 == 'cancelar':
            print('=================')
            ask()
        else:
            res2 = int(res2)
        if quanti_found > res2:
            res3 = quanti_found - res2
            quantidades.pop(prod_found)
            quantidades.insert(prod_found, res3)
    else:
        print('Produto não encontrado')
        print('Tente novamente')
        remove_produto()
    historico.append(f'{res2} unidades do produto {res1} foi removido do estoque!')
    print(historico[-1])   
    print('=================')
    ask()


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






