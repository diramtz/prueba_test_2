from svd import sign
#from svd import ortogonalidad
from random import random

def test_sign():
	"""Test para la funcion auxiliar sign del algortimo svd"""
	n = random()
	assert sign(n**2) == 1
	assert sign((-1)*(n**2)) == -1
