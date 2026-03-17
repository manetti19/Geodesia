#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 13:33:15 2026

@author: roberto
"""

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Parâmetro de deformação
# -----------------------------
a = 0.45

# -----------------------------
# Malha
# -----------------------------
x = np.linspace(-2.8, 2.8, 700)
y = np.linspace(-2.8, 2.8, 700)
X, Y = np.meshgrid(x, y)

# -----------------------------
# Funções
# f(z) = z - (a/3) z^3
# u = Re(f), v = Im(f)
# -----------------------------
U = X - (a/3)*X**3 + a*X*Y**2
V = Y - a*X**2*Y + (a/3)*Y**3

# -----------------------------
# Figura
# -----------------------------
#plt.figure(figsize=(9, 8))
plt.figure(figsize=(7, 7))

# Curvas de nível do "terreno"
levels_u = np.linspace(U.min()*0.65, U.max()*0.65, 18)
#levels_u = np.linspace(U.min(), U.max(), 18)
cu = plt.contour(X, Y, U, levels=levels_u, colors='saddlebrown', linewidths=1.0)

# Curvas azuis: linhas ortogonais com cara de drenagem
# #levels_v = [-1.6, -1.0, -0.5, 0.0, 0.5, 1.0, 1.6]
# levels_v = [1.2]
# cv = plt.contour(X, Y, V, levels=levels_v, colors='b', linewidths=1.8)

# Destacar a linha central
plt.contour(X, Y, V, levels=[0], colors='navy', linewidths=2.6)

# Eixos
plt.xlim(0,3)
plt.ylim(0,3)
plt.axhline(0, color='k', linewidth=0.6)
plt.axvline(0, color='k', linewidth=0.6)

plt.gca().set_aspect('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Terreno idealizado: $u(x,y)$ (sepia) e linhas ortogonais $v(x,y)$ (azul)')

plt.show()