class Conta:
	

## exercicio 2 lista 6

	saldo = None

	def __init__(self, saldo):
		
		self.saldo= saldo


	def imprimir_saldo(self):
		print(self.saldo)


	def depositar(self, valor):
		self.saldo = self.saldo+valor


	def retirar(self, valor):
		if(self.saldo > valor):
			self.saldo = self.saldo-valor


	def get_saldo(self):
		return self.saldo






