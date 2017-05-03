
class Gato(object):
	"""docstring for Gato"""
	def __init__(self):
		
		self.nombre = ""
		self.peso = 0
		self.edad = 0


	def miau(self):
		print("Miauuuu")


pelusa1 = Gato()
pelusa1.nombre = "Pelusa"
pelusa1.peso = 2
pelusa1.edad = 2

pelusa1.miau()