class Categoria:
   Max_categoria = 5


   def __init__(self, nome_categoria, _porcentagem_lucro):
       self.nome_categoria = nome_categoria.upper()
       self.porcentagem = _porcentagem_lucro


   @staticmethod
   def cadastrar_categoria (categorias, Max_categoria):
       nome_categoria = input('Digite o nome da categoria.\n')
       porcentagem_lucro = float(input('Digite a porcentagem de lucro dessa categoria:\n'))
       if len(categorias) == Max_categoria:
           return print('Só é possivel cadastrar 5 categorias:')
       if nome_categoria != '':
           cat_nome = Categoria(nome_categoria, porcentagem_lucro)
           categorias.append(cat_nome)


   @staticmethod
   def excluir_categoria(categorias):
       nome_categoria = input('Digite o nome da categoria de deseja excluir:\n')
       for list_cat in categorias:
           if nome_categoria == list_cat.nome_categoria:
               categorias.remove(list_cat)
               print('Categoria excluida com sucesso!', list_cat, )


   @staticmethod
   def exibir_categoria(categorias):
       for cat in categorias:
           print(cat)


   def __str__(self):
       return self.nome_categoria