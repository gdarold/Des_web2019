from ingresso import Ingresso


# exercicio 1 lista 6

class Ingresso_vip(Ingresso):

	adicional_vip = None

	def __init__(self, adicional):
		self.adicional_vip = self.get_valor()+adicional


	def imprimir_ingresso_vip(self):

		print("Ingresso vip ",self.adicional_vip)




