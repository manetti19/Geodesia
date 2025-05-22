#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:49:34 2025

@author: roberto
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
# ----------------------------
# Parâmetros do elipsoide WGS84
# ----------------------------
a = 6378137.0             # semi-eixo maior (m)
e2 = 0.00669438002290           # excentricidade ao quadrado

# ----------------------------
# Funções do raio de curvatura
# ----------------------------
def M(phi):
    return a * (1 - e2) / (1 - e2 * np.sin(phi)**2)**(3/2)

def r(phi):
    return a * np.cos(phi) / np.sqrt(1 - e2 * np.sin(phi)**2)

# ----------------------------
# Sistema de EDOs: phi', lambda', alpha'
# ----------------------------
def sistema_geodesico(s, y):
    phi, lambd, alpha = y
    dphi_ds = np.sin(alpha) / M(phi)
    dlambd_ds = np.cos(alpha) / (r(phi) * 1/np.cos(phi))  # sec(phi) = 1/cos(phi)
    dalpha_ds = -np.sin(phi) * np.cos(alpha) / r(phi)
    return [dphi_ds, dlambd_ds, dalpha_ds]

# ----------------------------
# Condições iniciais
# ----------------------------
phi0 = np.radians(0.0)         # latitude inicial (rad)
lambd0 = np.radians(0.0)       # longitude inicial (rad)
alpha0 = np.radians(45.0)      # azimute inicial (rad)

y0 = [phi0, lambd0, alpha0]

# Intervalo de integração (s em metros)
s_span = (0, 24500000)          # até 2000 km
ds = 500.0
s_eval = np.arange(s_span[0], s_span[1] + ds, ds)

# ----------------------------
# Solução numérica
# ----------------------------
sol = solve_ivp(sistema_geodesico, s_span, y0, t_eval=s_eval, method='RK45')

phi_sol = sol.y[0]
lambd_sol = sol.y[1]



# Converter para graus
phi_f_deg = math.degrees(phi_sol[-1])
lamda_f_deg = math.degrees(lambd_sol[-1])

print("Ponto final em coordenadas geodésicas:")
print(f"Latitude  (phi)  = {phi_f_deg:.6f}°")
print(f"Longitude (lambda) = {lamda_f_deg:.6f}°")

# ----------------------------
# Conversão para coordenadas 3D (x, y, z)
# ----------------------------
def geodesica_to_cartesiano(phi, lambd):
    N = a / np.sqrt(1 - e2 * np.sin(phi)**2)
    x = N * np.cos(phi) * np.cos(lambd)
    y = N * np.cos(phi) * np.sin(lambd)
    z = (N * (1 - e2)) * np.sin(phi)
    return x, y, z

x, y, z = geodesica_to_cartesiano(phi_sol, lambd_sol)

# ----------------------------
# Geração do elipsoide 3D para visualização
# ----------------------------
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-np.pi/2, np.pi/2, 100)
U, V = np.meshgrid(u, v)

# Coordenadas do elipsoide
X = a * np.cos(V) * np.cos(U)
Y = a * np.cos(V) * np.sin(U)
Z = a * (1 - e2) * np.sin(V)

# # ----------------------------
# # Plot 3D
# # ----------------------------
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')

# # Desenha o elipsoide
# ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.3, linewidth=0)

# # Trajetória da geodésica
# ax.plot3D(x, y, z, color='red', linewidth=2, label='Geodésica')

# # Ponto inicial
# ax.scatter(x[0], y[0], z[0], color='green', s=50, label='Início')

# ax.set_title('Geodésica sobre o Elipsoide WGS84', fontsize=14)
# ax.set_xlabel('X (m)')
# ax.set_ylabel('Y (m)')
# ax.set_zlabel('Z (m)')
# ax.legend()
# ax.set_box_aspect([1,1,0.8])  # proporção para elipsoide

# plt.tight_layout()
# plt.show()

# ----------------------------
# Geração da zona elipsoidal (faixa local)
# ----------------------------

# Determina faixa de latitudes e longitudes próximas à geodésica
phi_min, phi_max = np.min(phi_sol), np.max(phi_sol)
lambd_min, lambd_max = np.min(lambd_sol), np.max(lambd_sol)

# Margem extra para a zona elipsoidal
delta_phi = np.radians(3)     # 3 graus para cima e baixo
delta_lambda = np.radians(3)

# Geração da malha limitada
v = np.linspace(phi_min - delta_phi, phi_max + delta_phi, 100)
u = np.linspace(lambd_min - delta_lambda, lambd_max + delta_lambda, 100)
U, V = np.meshgrid(u, v)

# Superfície limitada do elipsoide (zona)
X = a * np.cos(V) * np.cos(U)
Y = a * np.cos(V) * np.sin(U)
Z = a * (1 - e2) * np.sin(V)

# ----------------------------
# Plot 3D apenas da zona
# ----------------------------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plota a zona elipsoidal
ax.plot_surface(X, Y, Z, color='lightgray', alpha=0.4, linewidth=0)

# Plota a geodésica
ax.plot3D(x, y, z, color='red', linewidth=2, label='Geodésica')

# Ponto inicial
ax.scatter(x[0], y[0], z[0], color='green', s=50, label='Início')

ax.scatter(x[-1], y[-1], z[-1], color='blue', s=60, label='Fim (ponto final)', zorder=12)


# Ajustes do gráfico
ax.set_title('Zona Elipsoidal com Geodésica', fontsize=14)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.legend()
ax.set_box_aspect([1,1,0.8])
# Ajuste da visão
ax.view_init(elev=20, azim=40)

plt.tight_layout()
plt.show()
