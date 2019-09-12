from conta import Conta


class Conta_poupanca(Conta):
	

	def __init__(self, saldo):
		Conta.__init__(self,saldo)
		

	def poupar(self):
		self.saldo = round(self.saldo*1.005,2)




		