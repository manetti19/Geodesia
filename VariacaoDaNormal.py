from scipy.integrate import quad
from scipy.optimize import root_scalar
import numpy as np

#A partir do equador, anda-se 2000 km ao longo de um meridiano.
#Qual foi a variação angular da normal em relação à superfície?
#(ou seja, quanto a normal girou no espaço tridimensional)

# Parâmetros do elipsoide WGS84
a = 6378137  # semi-eixo maior
f = 1 / 298.257223563
e2 = f * (2 - f)  # excentricidade ao quadrado

# Raio de curvatura meridional M(phi)
def M(phi):
    return a * (1 - e2) / (1 - e2 * np.sin(phi)**2)**(3/2)

# Integral de M de 0 até phi (em radianos)
def L(phi):
    result, _ = quad(M, 0, phi)
    return result

# Função objetivo: queremos L(phi) = 2.000.000 m
def objetivo(phi):
    return L(phi) - 2000000

# Resolver usando root_scalar
sol = root_scalar(objetivo, bracket=[0, np.pi/2], method='brentq')

# Resultado em graus
phi_graus = np.degrees(sol.root)
print(f"Ângulo de latitude correspondente a 2000 km: {phi_graus:.4f} graus")
