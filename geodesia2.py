import math
import pandas as pd
import matplotlib.pyplot as plt

# Constantes do elipsoide GRS80
a = 6378137.0  # raio equatorial em metros
e2 = 0.00669438002290  # excentricidade ao quadrado

# Dados iniciais
phi = math.radians(40.0)       # latitude inicial em rad
lamb = math.radians(10.0)      # longitude inicial em rad
alpha = math.radians(60.0)     # azimute inicial em rad
delta_s = 10000                # incremento de 10 km em metros
n_iter = 10                    # total de 100 km

# Funções auxiliares
def M(phi):
    return a * (1 - e2) / (1 - e2 * math.sin(phi)**2)**1.5

def P(phi):
    return a * math.cos(phi) / math.sqrt(1 - e2 * math.sin(phi)**2)

# Lista de resultados
results = []
latitudes = []
longitudes = []

for i in range(n_iter + 1):
    lat_deg = math.degrees(phi)
    lon_deg = math.degrees(lamb)

    results.append({
        "Iteração": i,
        "Latitude (°)": lat_deg,
        "Longitude (°)": lon_deg
    })

    latitudes.append(lat_deg)
    longitudes.append(lon_deg)
    
    # Cálculo dos incrementos
    delta_phi = (math.cos(alpha) / M(phi)) * delta_s
    delta_lamb = (math.sin(alpha) / P(phi)) * delta_s

    # Atualização das coordenadas
    phi += delta_phi
    lamb += delta_lamb

# Converter para DataFrame e exibir
df = pd.DataFrame(results)
print(df)

# Plotar gráfico
plt.figure(figsize=(8, 6))
plt.plot(longitudes, latitudes, marker='o')
plt.title('Trajetória Geodésica (incrementos de 10 km)')
plt.xlabel('Longitude (°)')
plt.ylabel('Latitude (°)')
plt.grid(True)
plt.tight_layout()
plt.show()
