import numpy as np

# Valores fornecidos
a = 6378137.0  # Semi-eixo maior em metros
f = 1 / 298.257223563  # Achatamento
b = a * (1 - f)  # Semi-eixo menor
e = np.sqrt((a**2 - b**2) / a**2)  # Excentricidade

# Convertendo os valores de phi e lambda de graus para radianos
phi = np.radians(-22.956265)  # Latitude
lambda_ = np.radians(-43.165314)  # Longitude

# Cálculo de X, Y e Z diretamente
denom = np.sqrt(1 - e**2 * np.sin(phi)**2)
X = a * np.cos(phi) * np.cos(lambda_) / denom
Y = a * np.cos(phi) * np.sin(lambda_) / denom
Z = b * np.sin(phi) / denom

print(f"X: {X}, Y: {Y}, Z: {Z}")