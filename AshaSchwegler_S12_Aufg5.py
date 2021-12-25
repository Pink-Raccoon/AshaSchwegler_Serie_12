# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 22:50:42 2021

@author: Asha
"""



import numpy as np
import matplotlib.pyplot as plt

"""==================== INPUT ===================="""
A = np.array([[1,1,0], [3,-1,2],[2,-1,3]], dtype=np.float64)

v0 = np.array([1,0,0]).T
"""==============================================="""

def von_mises_iteration(A_in, v_in):
    A = np.copy(A_in)
    v = np.copy(v_in)
    eigv = 0
    tol = 1e-4
    i = 0

    values = []
    

    while True:
        v_next = (A @ v) / (np.linalg.norm(A @ v))
        eigv = (v.T @ A @ v) / (v.T @ v)
        v = v_next
        values.append(eigv)
        i +=1

        print("n = " + str(i) + ": λ = " + str(eigv))
        
        if np.linalg.norm (v_next-v) < tol:
            break 
        
    return eigv, v, values


ew, ev, values = von_mises_iteration(A, v0)
print("Grösster Eigenwert / Spektralradius = " + str(ew))
print("Zugehöriger Eigenvektor = " + str(ev))


print(np.linalg.eig(A))
