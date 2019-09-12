from conta_corrente import Conta_corrente
from conta_poupanca import Conta_poupanca
from conta_imposto import Conta_imposto
from conta import Conta



class teste:


	conta1 = Conta(100)


	conta1.imprimir_saldo()

	conta2 = Conta_corrente(1000)


	conta2.imprimir_saldo()

	conta2.depositar(150)

	conta2.retirar(100)


	conta2.imprimir_saldo()



	conta3 = Conta_poupanca(500)

	conta3.imprimir_saldo()

	conta3.poupar()

	conta3.imprimir_saldo()




	conta4 = Conta_imposto(500)
	conta4.calcular_imposto(5)
	conta4.imprimir_saldo()



