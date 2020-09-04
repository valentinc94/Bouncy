from itertools import *

class Bouncy():

	def __init__(self):
		nums = count(1)
		rebote = self.running_total(map(lambda n: float(self.is_rebote(n)), count(1)))
		boncy = next((n for n, b in zip(nums, rebote) if b / n == 0.99))
		print(boncy)

	def pareja(self, iterable):
        #s -> (s0,s1), (s1,s2), (s2, s3), (sn-1, sn)
        #La función tee() devuelve varios iteradores independientes (por defecto 2) basados en una sola entrada original
		a, b = tee(iterable)
        #La funcion next() cuando se le llama, devuelve la siguiente elemento en la secuencia, cuando no queda nada para ser devuelto, lanza la excepción
		next(b, None)
        #La función zip toma como argumento dos o más objetos iterables y retorna un nuevo iterable
		return zip(a, b)

	def digitos(self, n):
        #digitos me crea una lista que aplicara un map, este map toma una función y una lista y aplica esa función a cada elemento de esa lista, produciendo una nueva lista
		return list(map(int, str(n)))

	def is_aumentando(self, n):
        #esta funcion me retorno todos los elementos siempre y cuando el nº previo sea inferior o igual al actual
		return all(prev <= curr for prev, curr in self.pareja(self.digitos(n)))

	def is_disminuyendo(self, n):
        #esta funcion me retorno todos los elementos siempre y cuando el nº previo sea mayor o igual al actual
		return all(prev >= curr for prev, curr in self.pareja(self.digitos(n)))

	def is_rebote(self, n):
        #esta funcion me retorna los elementos que sean de tipo rebote es decir numeros enteros positivos que no aumenta ni disminuye un número
		return not self.is_aumentando(n) and not self.is_disminuyendo(n)

	def running_total(self, iterable):
		total = 0
		for element in iterable:
			total += element
			yield total

if __name__ == "__main__":
	prueba = Bouncy()