from bomba_combustivel import Bomba_combustivel


class teste:

	bomba1 = Bomba_combustivel("Gasolina",3.95,1000)

	bomba1.imprimir_status_bomba()

	bomba1.abastecer_por_valor(100)

	bomba1. abastecer_por_litro(50)

	bomba1.alterar_valor(4.05)

	bomba1.alterar_tipo_combustivel("Diesel") 
	bomba1.alterar_valor(2.90)

	bomba1.alterar_quantidade_combustivel_bomba(900)


	bomba1.imprimir_status_bomba()

	