import sys
import os
import numpy as np
from TSPInstance import TSPInstance

def main(argv):
    filename = 'data/dummy.tsp'
    distance = 500
    tspInstance = TSPInstance.readFile(filename, distance, True)
    assert tspInstance, 'Error al leer la instancia'
    print('Nodos:')
    print(tspInstance.nodes)
    print('Distancia a probar: ' + str(tspInstance.distance))
    print(tspInstance.distancias)

    cert = [0,1,2,3,4,5]
 #   cert = [0,2,4,1,3,5]

    acc = 0
    for i in range(0,5):
        acc+=tspInstance.distancias[cert[i], cert[i+1]]
    acc+=tspInstance.distancias[cert[5], cert[0]]

    print('distancia total:' + str(acc))

if __name__ == "__main__":
    main(sys.argv[1:])