import math
import pandas as pd

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

for i in range(n_iter + 1):
    results.append({
        "Iteração": i,
        "Latitude (°)": math.degrees(phi),
        "Longitude (°)": math.degrees(lamb)
    })
    
    # Cálculo dos incrementos
    delta_phi = (math.cos(alpha) / M(phi)) * delta_s
    delta_lamb = (math.sin(alpha) / P(phi)) * delta_s

    # Atualização das coordenadas
    phi += delta_phi
    lamb += delta_lamb

# Exibir como tabela (opcional, se estiver em Jupyter)
df = pd.DataFrame(results)
print(df)
