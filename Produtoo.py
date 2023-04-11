from Categoriaa import Categoria

class Produto(Categoria):
   quantidade_estoque =  0
   def __init__(self, nome_produto, _preco,  nome_categoria, _porcentagem_lucro):
       super().__init__(nome_categoria, _porcentagem_lucro)
       self.nome_produto = nome_produto
       self.quantidade_estoque = 0



   @staticmethod
   def cadastrar_produto(lista_produto, lista_categoria):
       cate = input('Digite qual categoria esse produto faz parte:\n').upper()
       nome_produto = input('Digite o nome do produto que deseja cadastra:\n')
       _preco = float(input('Digite o preço do produto: \n'))
       for cat in lista_categoria:
           if nome_produto != '':
               if cate == cat.nome_categoria:
                   valor_final = ((cat.porcentagem/100)* _preco) + _preco
                   print('O valor final é de :', valor_final)
                   prod_nome = Produto(nome_produto, valor_final, cat.nome_categoria, cat.porcentagem)
                   lista_produto.append(prod_nome)
                   print('Produto cadastrado {} R$:{}, quantidade:{}.'.format(nome_produto, valor_final, prod_nome.quantidade_estoque))


   @staticmethod
   def excluir_produto(lista_produto, quantidade_estoque):
       nome_produto = input('Digite o nome do produto de deseja excluir:\n')
       for list in lista_produto:
           if nome_produto == list.nome_produto:
               lista_produto.remove(list)
               print('Produto excluido com sucesso!', list.nome_produto)


   @staticmethod
   def exibir_produto(lista_produto):
       for prod in lista_produto:
           print('Produto {}, Estoque {}'.format(prod.nome_produto, prod.quantidade_estoque))


   @staticmethod
   def adiciona_estoque_produto(lista_produto):
       prodt = input('Digite o produto que deseja adicionar o estoque: \n')
       estoque = int(input('Digite a quantidade em estoque: \n'))
       for i in lista_produto:
           if prodt == i.nome_produto:
               i.quantidade_estoque = i.quantidade_estoque + estoque
               print('A quantidade em estoque é{} do produto {}'.format(i.quantidade_estoque, i.nome_produto))


   @staticmethod
   def remove_estoque_produto(lista_produto):
       remove_prodt = input('Digite o produto que deseja excluir o estoque:\n')
       remove_estoque = int(input('Digite a quantidade que deseja excluir do estoque:\n'))
       for ii in lista_produto:
           if remove_prodt == ii.nome_produto:
               ii.quantidade_estoque = ii.quantidade_estoque - remove_estoque
               print('A quantidade em estoque é{} do produto {}'.format(ii.quantidade_estoque, ii.nome_produto))


   '''def __str__(self,  _nome_produto, _custo_compra, _quantidade_estoque,_nome_categoria):
   return f"Produto{_nome_produto}, categoria {_nome_categoria}, {_quantidade_estoque} em estoque, preço de venda R$ {_valor_venda} "'''
