from Produtoo import Produto
from Categoriaa import Categoria

lista_categoria = []

lista_produto = []

while True:

   print("MENU PRINCIPAL")
   print("1 - Cadastrar Categoria")
   print("2 - Excluir Categoria")
   print("3 - Cadastrar Produto")
   print("4 - Excluir Produto")
   print("5 - Exibir Produtos Cadastrados")
   print("6 - Adicionar Estoque a Produto")
   print("7 - Remover Estoque de Produto")
   print("8 - Sair")
   print("")
   opcao = input("Informe a opção desejada:\n ")


   if opcao == "1":
       Categoria.cadastrar_categoria(lista_categoria, Max_categoria=5)
   elif opcao == "2":
       Categoria.excluir_categoria(lista_categoria)
   elif opcao == "3":
       Produto.cadastrar_produto(lista_produto, lista_categoria)
   elif opcao == "4":
       Produto.excluir_produto(lista_produto, lista_categoria)
   elif opcao == "5":
       Produto.exibir_produto(lista_produto)
   elif opcao == "6":
       Produto.adiciona_estoque_produto(lista_produto)
   elif opcao == "7":
       Produto.remove_estoque_produto(lista_produto)
   elif opcao == "8":
       break
   else:
       print("Opção inválida. Tente novamente.")


Categoria.exibir_categoria(lista_categoria)

