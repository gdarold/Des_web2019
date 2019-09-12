from conta_corrente import Conta_corrente

class Conta_imposto(Conta_corrente):
	

	def __init__(self, saldo):
		Conta_corrente.__init__(self,saldo)
		


	def calcular_imposto(self, imposto):
		self.saldo = self.saldo-((self.saldo*imposto)/100)

