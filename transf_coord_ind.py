import math

def ecef_to_geodetic(X, Y, Z, a=6378137.0, f=1/298.257223563, tol=1e-12):
    # Longitude
    lamb = math.atan2(Y, X)

    # Parâmetros do elipsoide
    b = a * (1 - f)
    e2 = (a**2 - b**2) / a**2
    ep2 = (a**2 - b**2) / b**2

    # Cálculo inicial
    p = math.sqrt(X**2 + Y**2)
    theta = math.atan2(Z * a, p * b)

    # Latitude inicial (método de Bowring)
    phi = math.atan2(Z + ep2 * b * math.sin(theta)**3,
                     p - e2 * a * math.cos(theta)**3)

    # Iteração para refinar latitude
    prev_phi = 0
    while abs(phi - prev_phi) > tol:
        prev_phi = phi
        N = a / math.sqrt(1 - e2 * math.sin(phi)**2)
        h = p / math.cos(phi) - N
        phi = math.atan2(Z, p * (1 - e2 * (N / (N + h))))

    # Cálculo final de altura
    N = a / math.sqrt(1 - e2 * math.sin(phi)**2)
    h = p / math.cos(phi) - N

    # Conversão para graus
    phi_deg = math.degrees(phi)
    lamb_deg = math.degrees(lamb)

    return phi_deg, lamb_deg, h

# Exemplo de uso:
x, y, z = 4203261.612, -4507446.233, -1640358.959
phi, lamb, h = ecef_to_geodetic(x, y, z)
print(f"Latitude: {phi:.8f}°\nLongitude: {lamb:.8f}°\nAltura: {h:.3f} m")
