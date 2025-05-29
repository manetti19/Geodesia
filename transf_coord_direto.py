import math

def geodetic_to_ecef(phi_deg, lambda_deg, h, a=6378137.0, f=1/298.257223563):
    # Conversão para radianos
    phi = math.radians(phi_deg)
    lamb = math.radians(lambda_deg)
    
    # Cálculo de parâmetros do elipsoide
    b = a * (1 - f)
    e2 = (a**2 - b**2) / a**2

    # Raio de curvatura na vertical
    N = a / math.sqrt(1 - e2 * math.sin(phi)**2)

    # Cálculo das coordenadas ECEF
    X = (N + h) * math.cos(phi) * math.cos(lamb)
    Y = (N + h) * math.cos(phi) * math.sin(lamb)
    Z = (N * (1 - e2) + h) * math.sin(phi)

    return X, Y, Z

# Exemplo de uso:
phi = -15.0       # latitude em graus
lamb = -47.0      # longitude em graus
h = 1000          # altura em metros

x, y, z = geodetic_to_ecef(phi, lamb, h)
print(f"Coordenadas ECEF:\nX = {x:.3f} m\nY = {y:.3f} m\nZ = {z:.3f} m")
