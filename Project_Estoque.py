produtos = ['bolo', 'pudim', 'agua']
quantidades = [20, 30, 40]
historico = ['20 unidades do produto bolo foi adicionado ao estoque!', '30 unidades do produto pudim foi adicionado ao estoque!', '40 unidades do produto agua foi adicionado ao estoque!']


def add_produto():
    print('=================')
    print('Digite "cancelar" para voltar!')
    new_prod = input('Qual produto desejá adicionar: ')
    if new_prod == 'cancelar':
        print('=================')
        ask()
    elif new_prod in produtos:
        print('=================')
        print(f'Produto {new_prod} já está na lista!')
        print('tente novamente!')
        ask()
    new_prod_quanti = int(input('Qual a quantidade desse produto: '))
    if new_prod_quanti < 0:
        print('=================')
        print('Não é possivel adicionar valor menor que 0')
        print('tente novamente!')
        ask()
    else:    
        produtos.append(new_prod)    
        quantidades.append(new_prod_quanti)
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
    res1 = input('Qual produto desejá ajustar: ')
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
        res2 = input('Qual a quantidade deseja ajustar: ')
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


def ver_produtos():
    print('=================')
    q = 0
    for produto in produtos:
        print(f'O produto {produto} tem {quantidades[q]} unidades em estoque!')
        q += 1
    print('=================')  
    ask()   


def hist():
    print('=================')
    for hist in historico:
        print(hist)
    print('=================')
    ask()
    

def ask():
    print('1. Adicionar produto')
    print('2. Ajustar produtos em estoque')
    print('3. Ver lista de produtos')
    print('4. Historio de operações')
    res = input('Escolha uma das opções: ')
    if type(res) is str:
        print('=================')
        print('Digite somente o codigo da opção desejada')
        print('Tente novamente!')
        ask()
    if int(res) == 1:
        add_produto()
    elif int(res) == 2:
        remove_produto()
    elif int(res) == 3:
        ver_produtos()
    elif int(res) == 4:
        hist()
    else:
        print('Resposta invalida!!')
        print('Tente novamente!')
        ask() 
    
        


ask()






