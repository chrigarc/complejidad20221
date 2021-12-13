# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:05:10 2020

@author: OscarHC
"""
from TSPInstance import TSPInstance
import numpy as np
import math
import time

class TSPSol:
  
  def __init__(self, instance, perm=None, permRandom=False, evaluar=True):
    self.instance = instance    
    self.dim = instance.dim
    self.perm = np.array(range(self.dim))
    self.eval = float("inf")
    
    if perm is not None:
      self.perm = np.array(perm)
    elif permRandom:
      self.randomSol()
      
    self.distancias = instance.distancias
    self.evaluacion = np.zeros(self.dim, dtype='float64')
    
    if evaluar:
       self.evaluar()
       
  def initRandomSol(instance):
    return TSPSol(instance, permRandom=True, evaluar=False)
    
  def randomSol(self):
    self.perm = np.random.permutation(self.dim)

  def evaluar(self):    
    # Calcular la suma de las distancias entre las ciudades
    self.eval = 0
    nodos = self.instance.nodes
    for i in range(self.dim-1):
      self.evaluacion[i] = self.distancias[self.perm[i]][self.perm[i+1]]
      self.eval += self.evaluacion[i]
    self.evaluacion[self.dim - 1] = self.distancias[self.perm[0]][self.perm[self.dim - 1]]
    self.eval += self.evaluacion[self.dim - 1]
    return self.eval
  
  def evaluar_swap(self, x, y, aplicar=False):
    (x, y) = (min(x, y), max(x, y))
    
    diff_eval = 0

    eval_suc_x = 0
    eval_pred_y = 0
    if (y != x + 1):
      eval_suc_x = self.distancias[self.perm[y]][self.perm[x+1]]
      eval_pred_y = self.distancias[self.perm[y-1]][self.perm[x]]
    else:
      eval_suc_x = self.evaluacion[x]
      eval_pred_y = self.evaluacion[y-1]
      
    diff_eval += eval_suc_x-self.evaluacion[x]    
    diff_eval += eval_pred_y-self.evaluacion[y-1]
  
    eval_pred_x = 0
    eval_suc_y = 0
    
    if x > 0:
      eval_pred_x = self.distancias[self.perm[x-1]][self.perm[y]]
      diff_eval += eval_pred_x-self.evaluacion[x-1]
    
    if y < (self.dim -1):
      eval_suc_y = self.distancias[self.perm[x]][self.perm[y+1]]
      diff_eval += eval_suc_y-self.evaluacion[y]      

    eval_fin = 0
    if x == 0:
      if y != self.dim-1:
        eval_fin = self.distancias[self.perm[self.dim-1]][self.perm[y]]
      else:
        eval_fin = self.evaluacion[self.dim - 1]
      
      diff_eval += eval_fin - self.evaluacion[self.dim-1]
    
    if y == (self.dim-1):
      if x != 0:
        eval_fin = self.distancias[self.perm[x]][self.perm[0]]
      else:
        eval_fin = self.evaluacion[self.dim - 1]
        
      diff_eval += eval_fin - self.evaluacion[self.dim-1]
      
    new_eval = self.eval + diff_eval
      
    if aplicar:
      self.evaluacion[x] = eval_suc_x
      self.evaluacion[y-1] =  eval_pred_y
      if x > 0:
        self.evaluacion[x-1] = eval_pred_x
      if y < (self.dim - 1):
        self.evaluacion[y] = eval_suc_y
      
      if x== 0 or y == (self.dim - 1):
        self.evaluacion[self.dim-1] = eval_fin
        
      self.eval = new_eval
      
      tmp = self.perm[x]
      self.perm[x] = self.perm[y]
      self.perm[y] = tmp
  
    return new_eval
    
  def getEval(self):
    self.evaluar()
    return np.sum(self.evaluacion)

  def __lt__(self, other):
    return self.eval < other.eval
      
  def imprimirGenes(self, genes, imprimir=True):
    strSol = ""
    strSol += str(genes[0:5]) + "..." \
      + str(genes[(self.dim - 5):(self.dim)])
    if imprimir: print(strSol)  
    return strSol
  
  def __str__(self):
    strSol = ""
    # strSol += "Sol: " + str(self.perm) + "\n"
    strSol += "Eval: " + str(self.eval) \
      + ", perm: " + self.imprimirGenes(self.perm, imprimir=False)
    return strSol