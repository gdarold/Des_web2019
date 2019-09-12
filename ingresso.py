class Ingresso:
	
# exercicio 1 lista 6
	__valor_em_reais = 50

	def __init__(self, valor):
		self.__valor_em_reais = valor



	def imprimir_valor_ingresso(self):
		print("ingresso normal",self.__valor_em_reais)
	
	def get_valor(self):
		return self.__valor_em_reais


