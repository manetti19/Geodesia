import numpy as np

def ponto_fixo(X, Y, Z, a, b, tol=1e-10, max_iter=1000):

    # Inicializa lambda
    lambda_ = np.arctan2(Y, X)  # Usando arctan2 para obter o valor correto de lambda
    phi_0 = -20
    phi = phi_0

    for _ in range(max_iter):

        # Inicializa phi com um valor de partir, considerando Z
        phi_novo = np.arcsin(((Z * np.sqrt( a**2 * np.cos(phi) **2 + b**2 * np.sin(phi) **2)) / (a * b)))

        # Verifica a convergência
        if np.allclose([phi], [phi_novo], atol=tol):
            break
        
        # Atualiza phi e lambda
        phi = phi_novo

    return np.degrees(phi), np.degrees(lambda_)  # Converte de radianos para graus

# Valores fornecidos
X = 4285853.505555057
Y = -4019804.5050739734
Z = -2480577.1628146167
a = 6378137.0  # Semi-eixo maior em metros
f = 1 / 298.257223563  # Achatamento
b = a * (1 - f)  # Semi-eixo menor

# Chamando a função
phi, lambda_ = ponto_fixo(X, Y, Z, a, b)
print(f"phi: {phi}, lambda: {lambda_}")