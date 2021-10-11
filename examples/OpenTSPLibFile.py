import sys

typeWeight = ''
nodeCoord = False
nodeWeight = False
dim = 0
name = ''

fileName = 'data/a280.tsp'

with open(fileName, "r") as data:
    lineNumber = 0
    lineWeight = 0
    for line in data:
        lineNumber += 1
        try:
            if line.startswith('EOF'): continue
            if line.startswith('COMMENT'): continue
            if nodeCoord:
                line = line.strip()
                line = line.replace("   ", " ")
                line = line.replace("  ", " ")
                coords = line.split(' ')
                id = int(coords[0].strip())
                print(str(id) + ", " + str(float(coords[1].strip())) + ",  " +str(float(coords[2].strip())) )
            elif line.startswith('NAME'):
                name = line.split(':')[1].strip()
            elif line.startswith('TYPE'):
                typeInst = line.split(':')[1].strip()
                assert typeInst == 'TSP', 'El tipo de instancia debe ser TSP'
            elif line.startswith('DIMENSION'):
                dim = int(line.split(':')[1].strip())
            elif line.startswith('EDGE_WEIGHT_TYPE'):
                typeWeight = line.split(':')[1].strip()
            elif line.startswith('NODE_COORD_SECTION'):
                assert dim > 0, 'Se debe indicar una dimensión mayor a cero'
                nodeCoord = True
                continue
            elif line.startswith('EDGE_WEIGHT_SECTION'):
                nodeWeight = True
                continue
        except:
            print("Ocurrió un error al procesar el archivo")
            print("linea " + str(lineNumber) + ":")
            print(line)
            print("Verifique que el archivo tenga el formato correcto.")
            print("Unexpected errors:")
            print(sys.exc_info())
assert dim > 0, 'No se pudo leer los datos de la instancia TSP'

print('Name: ' + str(name))
print("Numero de Vertices: " + str(dim))