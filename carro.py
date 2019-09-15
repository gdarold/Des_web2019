class Carro:
	"""docstring for Carro"""


	__tanque = None
	__consumo_km = None

	def __init__(self, consumo):
		self.__consumo_km = consumo
		self.__tanque = 0
		

	def adicionar_gasolina(self, quantidade):
		if((self.__tanque+quantidade)<=55):
			self.__tanque = self.__tanque+quantidade
		else:
			print("o tanque é limitado a 55 lts")


	def obter_galolina(self):
		print("Resta no tanque do carro", self.__tanque, " lts")

	def andar(self, distancia):

		self.vai_anda = distancia/self.__consumo_km
		if(self.vai_anda< self.__tanque):
			print("boa viagem")
			self.__tanque = self.__tanque-self.vai_anda


		else:
			print("não tem combustivel para esta viagem")

	
		