import numpy as np


class TSPRecocidoSimulado:
    # 0 - vecindadAdjacentes
    # 1 - vecindadCualquierCambio
    def __init__(self, sol, temperatura=1, limite = 100):
        self.sol = sol
        self.temperatura = temperatura
        self.MAX = limite

    def vecindadAdjacentes(self, sol):
        combinaciones = []
        for i in range(sol.dim - 1):
            combinaciones.append((i, i + 1))
        combinaciones.append((0, sol.dim - 1))
        return combinaciones

    def explora_vecindad(self):
        combinaciones = []
        combinaciones = TSPRecocidoSimulado.vecindadAdjacentes(self, sol=self.sol)

        np.random.shuffle(combinaciones)
        (x, y) = combinaciones[0]
        evaluacion = self.sol.evaluar_swap(x, y)
        return ((x, y), evaluacion)

    def aplicar_swap(self, x, y):
        return self.sol.evaluar_swap(x, y, aplicar=True)

    def busqueda_local(self):
        best_eval = self.sol.eval
        i = 0
        while i < self.MAX:
            i += 1
            print("- Sol Iter: " + str(i) + ", " + str(self.sol) + ' temp: ' + str(self.temperatura))
            ((x, y), eval_mov) = self.explora_vecindad()
            if eval_mov < best_eval:
                best_eval = self.aplicar_swap(x, y)
            elif self.aceptarMovimiento(eval_mov, best_eval):
                best_eval = self.aplicar_swap(x, y)    
        return self.sol

    def aceptarMovimiento(self, eval_mov, best_eval):
        # p = 1 / ( 1 + exp( [ f(s’) - eval(s)] / T ) )
        p = 1 / ( 1 + np.exp( ( eval_mov - best_eval) / self.temperatura ) )
        random = np.random.random()
        #print('prob: ' + str(p) + ', random: ' + str(random))
        return random < p