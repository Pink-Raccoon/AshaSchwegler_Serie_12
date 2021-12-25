# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 18:56:47 2021

@author: Asha
"""

import numpy as np

"""==================== INPUT ===================="""
A = np.array([[1,-2,0], [2,0,1],[0,-2,1]], dtype=np.float64)


A_sym = np.array([[6,1,2,1,2],[1,5,0,2,-1],[2,0,5,-1,0],[1,2,-1,6,1],[2,-1,0,1,7]], dtype=np.float64)
"""==============================================="""

def AshaSchwegler_S12_Aufgabe4(A, k):
    A = np.copy(A)
    P = np.eye(A.shape[0])

    for i in range(k):
        Q, R = np.linalg.qr(A)
        A = R @ Q
        P = P @ Q

    return A, P


#a
A, P = AshaSchwegler_S12_Aufgabe4(A, 100)
print(A)

print("")

#b
A_sym, P = AshaSchwegler_S12_Aufgabe4(A_sym, 1000)

print(A_sym)

print("")


#c
print(np.linalg.eig(A_sym))