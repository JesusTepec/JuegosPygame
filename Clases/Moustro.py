
def recucirResistencia(cantidad):
	monster.resistencia -= cantidad
	if monster.resistencia < 0:
		print ("The moster is dead :(")
	else:
		print (" JA Ja argg")

class Moustro(object):
	"""docstring for Moustro"""
	def __init__(self, nombre, resistencia):
		self.nombre = nombre
		self.resistencia = resistencia

monster = Moustro("Craven", 25)
recucirResistencia(5)
recucirResistencia(19)
recucirResistencia(6)