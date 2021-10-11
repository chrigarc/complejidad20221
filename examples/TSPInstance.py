import sys
import numpy as np

class TSPInstance:
  def __init__(self):
    self.name = ''
    self.dim = 0
    self.nodes = np.array([])
    self.distancias = np.zeros((self.dim, self.dim), dtype='float64')

  def setDim(self, dim):
    self.dim = dim
    self.nodes = np.array([None]*dim)
    self.distancias = np.zeros((self.dim, self.dim), dtype='float64')

  def addNode(self, id, x, y):
    assert id > 0 and id <= self.dim, 'Id Incorrecto para la dimensión del problema'
    self.nodes[id-1] = (x,y)

  def getNode(self, id):
    assert id > 0 and id <= self.dim, 'Id Incorrecto para la dimensión del problema'
    return self.nodes[id-1]

  def getDistance(self, id1, id2):
    return self.distancias[id1-1][id2-1]

  def calcularDistancias(self):
    nodos = self.nodes
    for i in range(self.dim):
      self.distancias[i][i] = 0
      for j in range(i):
        diffX = nodos[i][0] - nodos[j][0]
        diffY = nodos[i][1] - nodos[j][1]
        self.distancias[i][j] = np.sqrt(diffX*diffX + diffY*diffY)
        self.distancias[j][i] = self.distancias[i][j]

  def __str__(self):
    strObj= ""
    strObj += "Name: " + self.name + "\n"
    strObj += "Dim: " + str(self.dim) + "\n"
    return strObj
