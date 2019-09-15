

class Bomba_combustivel:
	"""docstring for Bomba_combustivel"""

	__tipo_combustivel = None
	__valor_litro = None
	__quantidade_combustivel = None
	

	def __init__(self, combustivel, valor_litro, quantidade):
		self.__tipo_combustivel = combustivel
		self.__valor_litro = valor_litro
		self.__quantidade_combustivel = quantidade

	
		
	def abastecer_por_valor(self, valor):

		self.__litros_abastecidos = valor/self.__valor_litro
		if(self.__quantidade_combustivel>self.__litros_abastecidos):

			print("Formam abastecidos ",self.__litros_abastecidos, " lts")
		else:
			print("Formam abastecidos ",self.__quantidade_combustivel, " lts")


	def abastecer_por_litro(self, litros):
		if(self.__quantidade_combustivel>litros):

			self.valor_total = litros*self.__valor_litro
			print("O valor total a ser pago ", round(self.valor_total),2)
		else:
			print("Formam abastecidos ",self.__quantidade_combustivel, " lts")



	def alterar_valor(self, valor):
		self.__valor_litro = valor
		print("Valor combustivel alterado")

	def alterar_tipo_combustivel(self, tipo):
		self.__tipo_combustivel = tipo
		print("Tipo de combustivel alterado")

	def alterar_quantidade_combustivel_bomba(self, valor):
		self.__quantidade_combustivel = self.__quantidade_combustivel +valor
		print("Total combustivel na bomba", self.__quantidade_combustivel)


		
	def imprimir_status_bomba(self):
		print("Tipo combustivel: ", self.__tipo_combustivel, "Valor por litro ", self.__valor_litro, "Total litros bomba ", self.__quantidade_combustivel)


